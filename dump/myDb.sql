CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    correo VARCHAR(40),
    usuario VARCHAR(40),
    contrasena VARCHAR(400)
);

CREATE TABLE Categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20)
);

CREATE TABLE Productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80),
    descripcion TEXT,
    precio DECIMAL(10, 2),
    stock INT,
    imagen VARCHAR(50),
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);

CREATE TABLE Ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    fecha_venta DATE,
    id_cliente INT,
    monto_total DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE DetallesVenta (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT,
    id_producto INT,
    cantidad INT,
    precio_total DECIMAL(10, 2),
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

INSERT INTO Categorias (nombre) VALUES ('Polos'),('Casacas'),('Gorras'),('Bebidas'),('Discos');

SET NAMES 'utf8mb4';

INSERT INTO Productos (nombre, imagen, descripcion, precio, stock, id_categoria)
VALUES
    ('Polo Blanco', 'tienda-1.png', 'Descripcion breve', 29.99, 50, 1),
    ('Chaqueta Marrón', 'tienda-2.png', 'Descripcion breve', 59.99, 30, 2),
    ('Polo Negro', 'tienda-3.png', 'Descripcion breve', 39.99, 40, 1),
    ('Chaqueta Crema', 'tienda-4.jpeg', 'Descripcion breve', 49.99, 20, 2),
    ('Chaqueta Negra', 'tienda-5.jpeg', 'Descripcion breve', 54.99, 25, 2),
    ('Polo Blanco', 'tienda-6.jpeg', 'Descripcion breve', 34.99, 35, 1),
    ('Gorra Blanca', 'tienda-7.jpeg', 'Descripcion breve', 19.99, 50, 3),
    ('Gorra Crema', 'tienda-8.jpeg', 'Descripcion breve', 21.99, 45, 3),
    ('Cantimplora', 'tienda-9.jpeg', 'Descripcion breve', 14.99, 60, 4),
    ('CD Armonia', 'tienda-10.jpg', 'Descripcion breve', 16, 20, 5);
