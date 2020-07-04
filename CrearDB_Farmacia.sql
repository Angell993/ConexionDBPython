CREATE DATABASE Farmacia;
	
use Farmacia;

DROP TABLE VENTAS;
DROP TABLE MEDICAMENTOS;
DROP TABLE CLIENTES;

CREATE TABLE MEDICAMENTOS(
	Id_medicamento int(5) NOT NULL AUTO_INCREMENT, 
	nombre_medicamento VARCHAR(25) NOT NULL,
	fcaducidad_medicamento DATE NOT NULL,
	indicaciones_medicamento VARCHAR(50) NOT NULL,
    PRIMARY KEY(Id_medicamento)
);
	   
CREATE TABLE CLIENTES(
	Id_cliente int(5) NOT NULL AUTO_INCREMENT,
	NumSegSocial_cliente VARCHAR(15) NOT NULL,
	Nombre_cliente VARCHAR(25) NOT NULL,
	Direccion_cliente VARCHAR(50) NOT NULL,
	Provincia_cliente VARCHAR(20) NOT NULL,
    PRIMARY KEY(Id_cliente)
);

CREATE TABLE VENTAS(
	Id_cliente INTEGER NOT NULL,
	Id_medicamento INTEGER NOT NULL,
	fVenta DATE NOT NULL,
	Sintomatologia_cliente VARCHAR(50),
    PRIMARY KEY(Id_cliente, Id_medicamento, fVenta)
);


	
INSERT INTO MEDICAMENTOS (Nombre_medicamento,fCaducidad_medicamento,Indicaciones_medicamento) VALUES('Ibuprofeno','2022-03-22','Para dolores de cabeza');	
INSERT INTO MEDICAMENTOS (Nombre_medicamento,fCaducidad_medicamento,Indicaciones_medicamento) VALUES('Paracetamol','2025-01-25','Para malestar general');
INSERT INTO MEDICAMENTOS (Nombre_medicamento,fCaducidad_medicamento,Indicaciones_medicamento) VALUES('Betadine','2027-02-20','Para desinfectar heridas');

INSERT INTO CLIENTES (NumSegSocial_cliente,Nombre_cliente,Direccion_cliente,Provincia_cliente) VALUES('1234','Jose','C/ Leganes, Fuenlabrada','Madrid');
INSERT INTO CLIENTES (NumSegSocial_cliente,Nombre_cliente,Direccion_cliente,Provincia_cliente) VALUES('4321','Luis','C/ Mostoles, Getafe','Madrid');
INSERT INTO CLIENTES (NumSegSocial_cliente,Nombre_cliente,Direccion_cliente,Provincia_cliente) VALUES('1324','David','C/ Getafe, Mostoles','Madrid');
INSERT INTO CLIENTES (NumSegSocial_cliente,Nombre_cliente,Direccion_cliente,Provincia_cliente) VALUES('4231','Ana','C/ Fuenlabrada, Leganes','Madrid');

INSERT INTO VENTAS (Id_cliente,Id_medicamento,fVenta,Sintomatologia_cliente) VALUES(1,3, '2022-01-20','Herida superficial'); 
INSERT INTO VENTAS (Id_cliente,Id_medicamento,fVenta,Sintomatologia_cliente) VALUES(1,1, '2020-02-11','Dolores de cabeza'); 
INSERT INTO VENTAS (Id_cliente,Id_medicamento,fVenta,Sintomatologia_cliente) VALUES(3,2, '2024-04-25','Gripe'); 
INSERT INTO VENTAS (Id_cliente,Id_medicamento,fVenta,Sintomatologia_cliente) VALUES(2,3, '2025-05-31','Herida'); 
INSERT INTO VENTAS (Id_cliente,Id_medicamento,fVenta,Sintomatologia_cliente) VALUES(4,2, '2030-03-27','Malestar general'); 


SELECT C.Nombre_cliente, C.NumSegSocial_cliente, M.Nombre_medicamento, V.fVenta, V.Sintomatologia_cliente
	FROM VENTAS V
	LEFT JOIN CLIENTES C ON V.Id_cliente = C.Id_cliente
	LEFT JOIN MEDICAMENTOS M ON V.Id_medicamento = M.Id_medicamento
	WHERE C.NumSegSocial_cliente = '1234'