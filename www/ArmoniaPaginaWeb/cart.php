<?php 
session_start(); 
//aqui empieza el carrito

	if(isset($_SESSION['carrito'])){
		$carrito_mio=$_SESSION['carrito'];
		if(isset($_POST['titulo'])){
			$id_producto=$_POST['id_producto'];
			$titulo=$_POST['titulo'];
			$precio=$_POST['precio'];
			$cantidad=$_POST['cantidad'];
			$producto_existente = false;

        // Verificar si el producto ya existe en el carrito
        foreach ($carrito_mio as $key => $item) {
            if ($item['titulo'] == $titulo) {
                $carrito_mio[$key]['cantidad'] += $cantidad;
                $producto_existente = true;
            }
        }

        // Si el producto no existe, agregarlo al carrito
        if (!$producto_existente) {
            $carrito_mio[] = array("titulo" => $titulo, "id_producto" =>$id_producto, "precio" => $precio, "cantidad" => $cantidad);
        }
    }
	}else{
		$id_producto=$_POST['id_producto'];
		$titulo=$_POST['titulo'];
		$precio=$_POST['precio'];
		$cantidad=$_POST['cantidad'];
		$carrito_mio[]=array("titulo"=>$titulo, "id_producto" =>$id_producto,"precio"=>$precio,"cantidad"=>$cantidad);	
	}
	

$_SESSION['carrito']=$carrito_mio;

//aqui termina el carrito


header("Location: ".$_SERVER['HTTP_REFERER']."");
?>



