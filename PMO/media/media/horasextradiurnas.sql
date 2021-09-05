CREATE TABLE `horasrecargonocturno` (
  `codigo` int(11) NOT NULL,
  `horaInicio` varchar(50) NOT NULL,
  `horaFin` varchar(50) NOT NULL,
  `cantidad` varchar(50) NOT NULL,
  `porcentaje` varchar(50) NOT NULL,
  `pago` varchar(50) NOT NULL,
  `trabajador_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `horasrecargonocturnodominical` (
  `codigo` int(11) NOT NULL,
  `horaInicio` varchar(50) NOT NULL,
  `horaFin` varchar(50) NOT NULL,
  `cantidad` varchar(50) NOT NULL,
  `porcentaje` varchar(50) NOT NULL,
  `pago` varchar(50) NOT NULL,
  `trabajador_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `horasrecargodiurnodominical` (
  `codigo` int(11) NOT NULL,
  `horaInicio` varchar(50) NOT NULL,
  `horaFin` varchar(50) NOT NULL,
  `cantidad` varchar(50) NOT NULL,
  `porcentaje` varchar(50) NOT NULL,
  `pago` varchar(50) NOT NULL,
  `trabajador_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `horasrecargonocturno` 
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `trabajador_id` (`trabajador_id`);

ALTER TABLE `horasrecargonocturnodominical` 
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `trabajador_id` (`trabajador_id`);

ALTER TABLE `horasrecargodiurnodominical` 
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `trabajador_id` (`trabajador_id`);


ALTER TABLE `horasrecargonocturno` 
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `horasrecargonocturnodominical` 
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `horasrecargodiurnodominical` 
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;


ALTER TABLE `horasrecargonocturno` 
  ADD FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador` (`codigoTrabajador`);

ALTER TABLE `horasrecargonocturnodominical` 
  ADD FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador` (`codigoTrabajador`);

ALTER TABLE `horasrecargodiurnodominical` 
  ADD` FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador` (`codigoTrabajador`);

