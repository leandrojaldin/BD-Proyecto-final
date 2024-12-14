def other_properties() -> str:
    return """-- 1. Modificar la tabla CLIENTE
ALTER TABLE CLIENTE
    MODIFY COLUMN ClienteID INT NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY (ClienteID),
    MODIFY COLUMN CI INT NOT NULL UNIQUE,
    MODIFY COLUMN Nombre VARCHAR(50) NOT NULL,
    MODIFY COLUMN Apellido VARCHAR(50) NOT NULL,
    MODIFY COLUMN Telefono INT UNIQUE,
    MODIFY COLUMN ModifiedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- Actualizar registros existentes para ModifiedDate
UPDATE CLIENTE SET ModifiedDate = CURRENT_TIMESTAMP;

-- Ajustar el AUTO_INCREMENT para que comience en el siguiente valor disponible
ALTER TABLE CLIENTE AUTO_INCREMENT = 11;

-- 2. Modificar la tabla SERVICIO
ALTER TABLE SERVICIO
    MODIFY COLUMN ServicioID INT NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY (ServicioID),
    MODIFY COLUMN Nombre VARCHAR(50) NOT NULL,
    MODIFY COLUMN HoraInicio TIME NOT NULL,
    MODIFY COLUMN HoraFin TIME NOT NULL,
    MODIFY COLUMN ModifiedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- Actualizar registros existentes para ModifiedDate
UPDATE SERVICIO SET ModifiedDate = CURRENT_TIMESTAMP;

-- Ajustar el AUTO_INCREMENT para que comience en el siguiente valor disponible
ALTER TABLE SERVICIO AUTO_INCREMENT = 5;

-- 3. Modificar la tabla INSCRIPCION
ALTER TABLE INSCRIPCION
    MODIFY COLUMN InscripcionID INT NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY (InscripcionID),
    MODIFY COLUMN ClienteID INT NOT NULL,
    ADD CONSTRAINT FK_ClienteID FOREIGN KEY (ClienteID) REFERENCES CLIENTE(ClienteID),
    MODIFY COLUMN CantidadMeses INT NOT NULL,
    MODIFY COLUMN FechaInicio DATE NOT NULL,
    MODIFY COLUMN FechaFin DATE GENERATED ALWAYS AS (DATE_ADD(FechaInicio, INTERVAL CantidadMeses MONTH)) STORED,
    MODIFY COLUMN Mensualidad INT NOT NULL DEFAULT 250,
    MODIFY COLUMN PrecioTotal INT GENERATED ALWAYS AS (Mensualidad * CantidadMeses) STORED,
    MODIFY COLUMN ModifiedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- Actualizar registros existentes para ModifiedDate
UPDATE INSCRIPCION SET ModifiedDate = CURRENT_TIMESTAMP;

-- Ajustar el AUTO_INCREMENT para que comience en el siguiente valor disponible
ALTER TABLE INSCRIPCION AUTO_INCREMENT = 11;

-- 4. Modificar la tabla PAGOS
ALTER TABLE PAGOS
    MODIFY COLUMN PagoID INT NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY (PagoID),
    MODIFY COLUMN InscripcionID INT NOT NULL,
    ADD CONSTRAINT FK_InscripcionID FOREIGN KEY (InscripcionID) REFERENCES INSCRIPCION(InscripcionID),
    MODIFY COLUMN Fecha DATE NOT NULL,
    MODIFY COLUMN Monto INT NOT NULL,
    MODIFY COLUMN ModifiedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- Actualizar registros existentes para ModifiedDate
UPDATE PAGOS SET ModifiedDate = CURRENT_TIMESTAMP;

-- Ajustar el AUTO_INCREMENT para que comience en el siguiente valor disponible
ALTER TABLE PAGOS AUTO_INCREMENT = 11;

-- 5. Modificar la tabla ASISTENCIA
ALTER TABLE ASISTENCIA
    MODIFY COLUMN AsistenciaID INT NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY (AsistenciaID),
    MODIFY COLUMN InscripcionID INT NOT NULL,
    ADD CONSTRAINT FK_Asistencia_InscripcionID FOREIGN KEY (InscripcionID) REFERENCES INSCRIPCION(InscripcionID),
    MODIFY COLUMN ServicioID INT NOT NULL,
    ADD CONSTRAINT FK_Asistencia_ServicioID FOREIGN KEY (ServicioID) REFERENCES SERVICIO(ServicioID),
    MODIFY COLUMN Fecha DATE NOT NULL,
    MODIFY COLUMN HoraIngreso TIME NOT NULL,
    ADD CONSTRAINT Unique_InscripcionID_Fecha UNIQUE (InscripcionID, Fecha),
    MODIFY COLUMN ModifiedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- Actualizar registros existentes para ModifiedDate
UPDATE ASISTENCIA SET ModifiedDate = CURRENT_TIMESTAMP;

-- Ajustar el AUTO_INCREMENT para que comience en el siguiente valor disponible
ALTER TABLE ASISTENCIA AUTO_INCREMENT = 11;

-- 6. Modificar la tabla ENTRENADORES
ALTER TABLE ENTRENADORES
    MODIFY COLUMN EntrenadorID INT NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY (EntrenadorID),
    MODIFY COLUMN ServicioID INT NOT NULL,
    ADD CONSTRAINT FK_Entrenadores_ServicioID FOREIGN KEY (ServicioID) REFERENCES SERVICIO(ServicioID),
    MODIFY COLUMN Nombre VARCHAR(50) NOT NULL,
    MODIFY COLUMN Apellido VARCHAR(50) NOT NULL,
    MODIFY COLUMN Telefono INT NOT NULL,
    MODIFY COLUMN Correo VARCHAR(50),
    MODIFY COLUMN FechaInicio DATE NOT NULL,
    MODIFY COLUMN FechaFin DATE,
    MODIFY COLUMN Sueldo INT NOT NULL,
    MODIFY COLUMN Turno VARCHAR(50),
    MODIFY COLUMN Estado VARCHAR(50) GENERATED ALWAYS AS (
        CASE WHEN FechaFin IS NULL THEN 'Activo' ELSE 'Despedido' END
    ) STORED,
    MODIFY COLUMN ModifiedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- Actualizar registros existentes para ModifiedDate
UPDATE ENTRENADORES SET ModifiedDate = CURRENT_TIMESTAMP;

-- Ajustar el AUTO_INCREMENT para que comience en el siguiente valor disponible
ALTER TABLE ENTRENADORES AUTO_INCREMENT = 9;
"""