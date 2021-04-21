#comentario de prueba
DELIMITER //
CREATE FUNCTION VERIFICAR_PRODUCTOS_REPETIDOS(NOMBRE CHAR(30), CANT_PRODUCTO INT(4)) RETURNS CHAR(100)
    BEGIN
    	#EN ESTA VARIABLE SE ALMACENARA LA CANTIDAD DE VECES QUE ESTA EL PRODUCTO EN LA BBDD
    	DECLARE PRODUCTO_ESTA INT(1) DEFAULT (SELECT COUNT(productos.ID) FROM productos 
                                              WHERE productos.NOMBRE = NOMBRE);
        
        IF PRODUCTO_ESTA != 0 THEN
        	RETURN CONCAT('EL PRODUCTO ', NOMBRE,' YA ESTA EN LA BBDD');
        ELSE
        	INSERT INTO productos
            SET productos.NOMBRE = NOMBRE, productos.CANTIDAD_PRODUCTOS = CANT_PRODUCTO;
        	RETURN CONCAT('SE HA INSERTADO EL PRODUCTO ',NOMBRE,' CON LA CANTIDAD DE ',CANT_PRODUCTO,' EXITOSAMENTE');
       END IF;
    END
//