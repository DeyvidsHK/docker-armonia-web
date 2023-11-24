<?php
session_start();

include 'conexion.php';

if (!isset($_SESSION['carrito']) || empty($_SESSION['carrito'])) {
    echo 'Error: El carrito está vacío.';
    exit();
}

$id_cliente = isset($_SESSION['id_cliente']) ? $_SESSION['id_cliente'] : 1;

$venta_data = array(
    "venta" => array(
        "id_cliente" => $id_cliente,
        "monto_total" => 0
    ),
    "detalleVenta" => array()
);

$baseURL = "http://core_api:8000/api/Sell/CreateSell";

mysqli_begin_transaction($conexion);

try {
    $fecha_venta = date('Y-m-d');
    $monto_total = 0;

    foreach ($_SESSION['carrito'] as $item) {
        $id_producto = $item['id_producto'];
        $cantidad = $item['cantidad'];
        $precio_total = $item['precio'] * $cantidad;

        $detalle_venta = array(
            "id_producto" => $id_producto,
            "cantidad" => $cantidad,
            "precio_total" => $precio_total
        );

        array_push($venta_data["detalleVenta"], $detalle_venta);

        $monto_total += $precio_total;
    }

    $venta_data["venta"]["monto_total"] = $monto_total;

    $json_data = json_encode($venta_data);

    // Enviar la solicitud a la API
    $options = [
        'http' => [
            'method' => 'POST',
            'header' => 'Content-Type: application/json',
            'content' => $json_data
        ]
    ];

    $context = stream_context_create($options);
    $result = file_get_contents($baseURL, false, $context);

    if ($result === FALSE) {
        throw new Exception('Error al enviar la solicitud a la API: ' . error_get_last()['message']);
    }

    // Decodificar la respuesta de la API si es necesario
    // $api_response = json_decode($result, true);

    mysqli_commit($conexion);

    unset($_SESSION['carrito']);

    header("Location: tienda.php");
    exit();
} catch (Exception $e) {
    mysqli_rollback($conexion);

    echo 'Error en el proceso de venta: ' . $e->getMessage();
} finally {
    mysqli_close($conexion);
}


?>
