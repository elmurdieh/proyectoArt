-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-07-2024 a las 16:26:27
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyectoartv1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `art`
--

CREATE TABLE `art` (
  `Art_id` int(5) NOT NULL,
  `Fecha_creacion` varchar(30) DEFAULT NULL,
  `Hora_creacion` varchar(30) DEFAULT NULL,
  `Estado_cierre` tinyint(1) DEFAULT NULL,
  `Supervisor_rut` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `art_res_sup`
--

CREATE TABLE `art_res_sup` (
  `Art_id` int(5) NOT NULL,
  `Supervisor_rut` varchar(12) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Cargo` varchar(100) NOT NULL,
  `Cond_trabajador` tinyint(1) NOT NULL,
  `Estado_firma` tinyint(1) NOT NULL,
  `Sup_asignado` varchar(100) NOT NULL,
  `Gerencia` varchar(100) NOT NULL,
  `Superintendencia` varchar(100) NOT NULL,
  `Trab_realizar` varchar(100) NOT NULL,
  `Lug_esp` varchar(100) NOT NULL,
  `Empresa` varchar(100) NOT NULL,
  `Fecha` varchar(30) NOT NULL,
  `Hora_inicio` varchar(15) NOT NULL,
  `Hora_termino` varchar(15) NOT NULL,
  `Pre_trans_1` tinyint(1) NOT NULL,
  `Pre_trans_2` tinyint(1) NOT NULL,
  `Pre_trans_3` tinyint(1) NOT NULL,
  `Pre_trans_4` tinyint(1) NOT NULL,
  `Pre_trans_5` tinyint(1) NOT NULL,
  `Pre_trans_6` tinyint(1) NOT NULL,
  `Trab_sim_1` tinyint(1) NOT NULL,
  `Trab_sim_2` varchar(100) NOT NULL,
  `Trab_sim_3` tinyint(1) NOT NULL,
  `Trab_sim_4` tinyint(1) NOT NULL,
  `Trab_sim_5` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `art_res_tra`
--

CREATE TABLE `art_res_tra` (
  `Art_id` int(5) NOT NULL,
  `Trabajador_rut` varchar(12) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Cargo` varchar(100) NOT NULL,
  `Condiciones_trabajador` tinyint(1) NOT NULL,
  `Pre_trans_1` tinyint(1) NOT NULL,
  `Pre_trans_2` tinyint(1) NOT NULL,
  `Pre_trans_3` tinyint(1) NOT NULL,
  `Pre_trans_4` tinyint(1) NOT NULL,
  `Pre_trans_5` tinyint(1) NOT NULL,
  `Pre_trans_6` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gerente`
--

CREATE TABLE `gerente` (
  `Nombre` varchar(300) NOT NULL,
  `Rut` varchar(12) NOT NULL,
  `Correo_electronico` varchar(300) NOT NULL,
  `Contraseña` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gerente`
--

INSERT INTO `gerente` (`Nombre`, `Rut`, `Correo_electronico`, `Contraseña`) VALUES
('gerente prueba', '12345678-9', 'gerentePrueba@ciquimet.com', '123456789');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `riesgos_criticos_sup`
--

CREATE TABLE `riesgos_criticos_sup` (
  `Art_id` int(5) NOT NULL,
  `Supervisor_rut` varchar(12) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Codigo` int(25) NOT NULL,
  `Riesgo_nro` int(25) NOT NULL,
  `Riesgo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `riesgos_criticos_tra`
--

CREATE TABLE `riesgos_criticos_tra` (
  `Art_id` int(5) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Codigo` int(25) NOT NULL,
  `Riesgo_nro` int(25) NOT NULL,
  `Riesgo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `supervisor`
--

CREATE TABLE `supervisor` (
  `Nombre` varchar(300) NOT NULL,
  `Rut` varchar(12) NOT NULL,
  `Correo_electronico` varchar(300) NOT NULL,
  `Contraseña` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `supervisor`
--

INSERT INTO `supervisor` (`Nombre`, `Rut`, `Correo_electronico`, `Contraseña`) VALUES
('Jose Juan', '26197953-1', 'whenhacestusmomosensql@ciquimet.com', 'Contraseña'),
('Pedro Poni', '26197953-2', 'QueJuegoHizoWillyrex@gmail.com', '31minutos'),
('supervisor prueba', '26197953-5', 'supervisorPrueba@ciquimet.com', 'Contraseña');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajador`
--

CREATE TABLE `trabajador` (
  `Nombre` varchar(300) NOT NULL,
  `Rut` varchar(12) NOT NULL,
  `Correo_electronico` varchar(300) NOT NULL,
  `Contraseña` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `trabajador`
--

INSERT INTO `trabajador` (`Nombre`, `Rut`, `Correo_electronico`, `Contraseña`) VALUES
('Ignacio', '20399562-1', 'kskskks@gmail.com', '0987654321'),
('Peppa pig', '26197953-7', 'ChangoleonItztapaluca@gmail.com', 'musicasMasEscuchadas2024'),
('trabajador prueba', '98765432-1', 'trabajadorPrueba@ciquimet.com', 'HomeroSimpson');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajadores_asignados`
--

CREATE TABLE `trabajadores_asignados` (
  `Art_id` int(5) NOT NULL,
  `Trabajador_rut` varchar(12) NOT NULL,
  `Estado_firma_trabajador` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `u_sinconfirmar`
--

CREATE TABLE `u_sinconfirmar` (
  `Nombre` varchar(100) NOT NULL,
  `Rut` varchar(12) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Correo_electronico` varchar(255) NOT NULL,
  `Rol` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `u_sinconfirmar`
--

INSERT INTO `u_sinconfirmar` (`Nombre`, `Rut`, `Contraseña`, `Correo_electronico`, `Rol`) VALUES
('Laptop Gamer', '26197952-1', 'uegho3rijgjsdngl', 'CoreaProfesor3@ciquimet.com', 'supervisor');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `art`
--
ALTER TABLE `art`
  ADD PRIMARY KEY (`Art_id`),
  ADD KEY `FK_SupervisorRut` (`Supervisor_rut`);

--
-- Indices de la tabla `art_res_sup`
--
ALTER TABLE `art_res_sup`
  ADD KEY `FK_ArtResSup_ArtId` (`Art_id`);

--
-- Indices de la tabla `art_res_tra`
--
ALTER TABLE `art_res_tra`
  ADD KEY `FK_ArtResTra_ArtId` (`Art_id`);

--
-- Indices de la tabla `gerente`
--
ALTER TABLE `gerente`
  ADD PRIMARY KEY (`Rut`);

--
-- Indices de la tabla `riesgos_criticos_sup`
--
ALTER TABLE `riesgos_criticos_sup`
  ADD KEY `fk_art_riesgos_sup` (`Art_id`);

--
-- Indices de la tabla `riesgos_criticos_tra`
--
ALTER TABLE `riesgos_criticos_tra`
  ADD KEY `fk_art_riesgos_tra` (`Art_id`);

--
-- Indices de la tabla `supervisor`
--
ALTER TABLE `supervisor`
  ADD PRIMARY KEY (`Rut`);

--
-- Indices de la tabla `trabajador`
--
ALTER TABLE `trabajador`
  ADD PRIMARY KEY (`Rut`);

--
-- Indices de la tabla `trabajadores_asignados`
--
ALTER TABLE `trabajadores_asignados`
  ADD KEY `FK_TrabajadoresAsignados_ArtId` (`Art_id`),
  ADD KEY `fk_trabajador_rut` (`Trabajador_rut`);

--
-- Indices de la tabla `u_sinconfirmar`
--
ALTER TABLE `u_sinconfirmar`
  ADD PRIMARY KEY (`Rut`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `art`
--
ALTER TABLE `art`
  MODIFY `Art_id` int(5) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `art`
--
ALTER TABLE `art`
  ADD CONSTRAINT `FK_SupervisorRut` FOREIGN KEY (`Supervisor_rut`) REFERENCES `supervisor` (`Rut`);

--
-- Filtros para la tabla `art_res_sup`
--
ALTER TABLE `art_res_sup`
  ADD CONSTRAINT `FK_ArtResSup_ArtId` FOREIGN KEY (`Art_id`) REFERENCES `art` (`Art_id`);

--
-- Filtros para la tabla `art_res_tra`
--
ALTER TABLE `art_res_tra`
  ADD CONSTRAINT `FK_ArtResTra_ArtId` FOREIGN KEY (`Art_id`) REFERENCES `art` (`Art_id`);

--
-- Filtros para la tabla `riesgos_criticos_sup`
--
ALTER TABLE `riesgos_criticos_sup`
  ADD CONSTRAINT `fk_art_riesgos_sup` FOREIGN KEY (`Art_id`) REFERENCES `art` (`Art_id`);

--
-- Filtros para la tabla `riesgos_criticos_tra`
--
ALTER TABLE `riesgos_criticos_tra`
  ADD CONSTRAINT `fk_art_riesgos_tra` FOREIGN KEY (`Art_id`) REFERENCES `art` (`Art_id`);

--
-- Filtros para la tabla `trabajadores_asignados`
--
ALTER TABLE `trabajadores_asignados`
  ADD CONSTRAINT `FK_TrabajadoresAsignados_ArtId` FOREIGN KEY (`Art_id`) REFERENCES `art` (`Art_id`),
  ADD CONSTRAINT `fk_trabajador_rut` FOREIGN KEY (`Trabajador_rut`) REFERENCES `trabajador` (`Rut`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
