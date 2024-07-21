-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-07-2024 a las 06:28:26
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
  `Art_id` int(50) NOT NULL,
  `Fecha_creacion` varchar(30) DEFAULT NULL,
  `Hora_creacion` varchar(30) DEFAULT NULL,
  `Estado_cierre` tinyint(1) DEFAULT NULL,
  `Supervisor_rut` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `art`
--

INSERT INTO `art` (`Art_id`, `Fecha_creacion`, `Hora_creacion`, `Estado_cierre`, `Supervisor_rut`) VALUES
(1, '2024-07-31', '18:16', NULL, '26197953-5'),
(4, '2024-07-21', '00:02:26', NULL, '26197953-5'),
(5, '2024-07-20', '21:04:30', NULL, '26197953-5'),
(6, '2024-07-20', '22:13:36', NULL, '26197953-5'),
(7, '2024-07-20', '22:27:46', NULL, '26197953-5'),
(8, '2024-07-20', '22:32:53', NULL, '26197953-5');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `art_res_sup`
--

CREATE TABLE `art_res_sup` (
  `Art_id` int(50) NOT NULL,
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

--
-- Volcado de datos para la tabla `art_res_sup`
--

INSERT INTO `art_res_sup` (`Art_id`, `Supervisor_rut`, `Nombre`, `Cargo`, `Cond_trabajador`, `Estado_firma`, `Sup_asignado`, `Gerencia`, `Superintendencia`, `Trab_realizar`, `Lug_esp`, `Empresa`, `Fecha`, `Hora_inicio`, `Hora_termino`, `Pre_trans_1`, `Pre_trans_2`, `Pre_trans_3`, `Pre_trans_4`, `Pre_trans_5`, `Pre_trans_6`, `Trab_sim_1`, `Trab_sim_2`, `Trab_sim_3`, `Trab_sim_4`, `Trab_sim_5`) VALUES
(4, '26197953-5', '', '', 0, 0, 'Robert', 'yo', 'WSS', 'mineria', 'mi casa', 'ciquimet', '2024-07-20', '21:31', '23:20', 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0),
(5, '26197953-5', '', '', 0, 0, 'yo', 'Choro', 'yo', 'las weas', 'mi casa', 'ciquimet', '2024-07-09', '21:04', '23:04', 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0),
(6, '26197953-5', '', '', 0, 0, 'EL WEA', 'yo', 'WSS', 'mineria', 'mi casa', 'ciquimet', '2024-07-30', '17:13', '23:13', 1, 1, 1, 1, 1, 0, 0, '', 0, 0, 0),
(8, '26197953-5', '', '', 0, 0, 'EL SHORO ROBERT', 'Choro', 'WSS', 'mineria', 'Laboratorio', 'ciquimet', '2024-07-03', '03:37', '00:37', 1, 1, 1, 1, 1, 1, 1, 'SI existe trabajo en simultaneo HOla', 1, 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `art_res_tra`
--

CREATE TABLE `art_res_tra` (
  `Art_id` int(50) NOT NULL,
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
  `Art_id` int(50) NOT NULL,
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
  `Art_id` int(50) NOT NULL,
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
('Robert Mauricio', '26197953-5', 'alvarezramirezr764@gmail.com', 'scrypt:32768:8:1$U0WaF8pkiFNyKq3W$843283c74c5b419a2d38eda571523af6469aa583c7cd4ffb849f78092fae501073cacfa0fae53160a71b62fa62deb960a907b24b0bfde628c7b7363c6e3d3d5f');

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
('male07', '26197953-1', 'correofalso1@ciquimet.com', 'scrypt:32768:8:1$bZSiTgHbqMiKMfut$231ca9ac28a388dc90f6619a9a1c80745f5fb724ef2ec2010e03a186e910208baf2fae2a13f67a012ffa5d4a50a78e85ecba0435f632ae291afff03f3e2ee6c0'),
('3060Ti edicion pendrive', '26197953-2', 'correofalso2@ciquimet.com', 'scrypt:32768:8:1$NT6GQ16FavFlH5GU$b3a194f3bb29f00ff5e0ec0dec0fdd2571542cd9b9d923672ee487b80bbf77907e6c3936c0241c94fe4e0e5f21966b07eee4fd1839274e2925e0b39d0ee2ef40'),
('Chocolate Trencito', '26197953-3', 'correofalso3@ciquimet.com', 'scrypt:32768:8:1$RGmpwpTrmRaiYNYD$e3df69695889a9abdeb75a4712b51d19f8fa8927d191f770a46af6bccb94ac85768ff649b65aed5f0c8c1fbc126f4fb89b65e8160be17c2a0f190f54860b0638');

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
  ADD KEY `FK_ArtResSup_ArtId` (`Art_id`),
  ADD KEY `Supervisor_rut` (`Supervisor_rut`);

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
  ADD KEY `fk_art_riesgos_sup` (`Art_id`),
  ADD KEY `Supervisor_rut` (`Supervisor_rut`);

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
  MODIFY `Art_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

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
  ADD CONSTRAINT `FK_ArtResSup_ArtId` FOREIGN KEY (`Art_id`) REFERENCES `art` (`Art_id`),
  ADD CONSTRAINT `art_res_sup_ibfk_1` FOREIGN KEY (`Supervisor_rut`) REFERENCES `supervisor` (`Rut`);

--
-- Filtros para la tabla `art_res_tra`
--
ALTER TABLE `art_res_tra`
  ADD CONSTRAINT `FK_ArtResTra_ArtId` FOREIGN KEY (`Art_id`) REFERENCES `art` (`Art_id`);

--
-- Filtros para la tabla `riesgos_criticos_sup`
--
ALTER TABLE `riesgos_criticos_sup`
  ADD CONSTRAINT `fk_art_riesgos_sup` FOREIGN KEY (`Art_id`) REFERENCES `art` (`Art_id`),
  ADD CONSTRAINT `riesgos_criticos_sup_ibfk_1` FOREIGN KEY (`Supervisor_rut`) REFERENCES `supervisor` (`Rut`);

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
