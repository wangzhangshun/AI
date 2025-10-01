/*
 Navicat Premium Data Transfer

 Source Server         : 本地8.0
 Source Server Type    : MySQL
 Source Server Version : 80404
 Source Host           : localhost:3307
 Source Schema         : words

 Target Server Type    : MySQL
 Target Server Version : 80404
 File Encoding         : 65001

 Date: 03/07/2025 21:54:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add user', 7, 'add_user');
INSERT INTO `auth_permission` VALUES (26, 'Can change user', 7, 'change_user');
INSERT INTO `auth_permission` VALUES (27, 'Can delete user', 7, 'delete_user');
INSERT INTO `auth_permission` VALUES (28, 'Can view user', 7, 'view_user');
INSERT INTO `auth_permission` VALUES (29, 'Can add word', 8, 'add_word');
INSERT INTO `auth_permission` VALUES (30, 'Can change word', 8, 'change_word');
INSERT INTO `auth_permission` VALUES (31, 'Can delete word', 8, 'delete_word');
INSERT INTO `auth_permission` VALUES (32, 'Can view word', 8, 'view_word');
INSERT INTO `auth_permission` VALUES (33, 'Can add question', 9, 'add_question');
INSERT INTO `auth_permission` VALUES (34, 'Can change question', 9, 'change_question');
INSERT INTO `auth_permission` VALUES (35, 'Can delete question', 9, 'delete_question');
INSERT INTO `auth_permission` VALUES (36, 'Can view question', 9, 'view_question');
INSERT INTO `auth_permission` VALUES (37, 'Can add test record', 10, 'add_testrecord');
INSERT INTO `auth_permission` VALUES (38, 'Can change test record', 10, 'change_testrecord');
INSERT INTO `auth_permission` VALUES (39, 'Can delete test record', 10, 'delete_testrecord');
INSERT INTO `auth_permission` VALUES (40, 'Can view test record', 10, 'view_testrecord');
INSERT INTO `auth_permission` VALUES (41, 'Can add test detail', 11, 'add_testdetail');
INSERT INTO `auth_permission` VALUES (42, 'Can change test detail', 11, 'change_testdetail');
INSERT INTO `auth_permission` VALUES (43, 'Can delete test detail', 11, 'delete_testdetail');
INSERT INTO `auth_permission` VALUES (44, 'Can view test detail', 11, 'view_testdetail');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$600000$RG4vNqweMtVaI3lTRveS0F$fn2gUZJpald1pTK9XwYbXwUzhj+W4wiRTtVb/tBpIe4=', '2025-06-29 12:08:48.665580', 1, 'lqz', '', '', '3@qq.com', 1, 1, '2025-06-26 14:08:35.658350');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (11, 'testsys', 'testdetail');
INSERT INTO `django_content_type` VALUES (10, 'testsys', 'testrecord');
INSERT INTO `django_content_type` VALUES (7, 'users', 'user');
INSERT INTO `django_content_type` VALUES (9, 'words', 'question');
INSERT INTO `django_content_type` VALUES (8, 'words', 'word');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2025-06-26 13:41:57.777665');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2025-06-26 13:41:58.007691');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2025-06-26 13:41:58.064193');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2025-06-26 13:41:58.069193');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-26 13:41:58.073716');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2025-06-26 13:41:58.119014');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2025-06-26 13:41:58.145658');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2025-06-26 13:41:58.159192');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2025-06-26 13:41:58.163704');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2025-06-26 13:41:58.187965');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2025-06-26 13:41:58.189687');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2025-06-26 13:41:58.194044');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2025-06-26 13:41:58.224150');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2025-06-26 13:41:58.272886');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2025-06-26 13:41:58.283938');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2025-06-26 13:41:58.288442');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2025-06-26 13:41:58.316993');
INSERT INTO `django_migrations` VALUES (18, 'sessions', '0001_initial', '2025-06-26 13:41:58.332343');
INSERT INTO `django_migrations` VALUES (19, 'words', '0001_initial', '2025-06-26 13:41:58.371094');
INSERT INTO `django_migrations` VALUES (20, 'users', '0001_initial', '2025-06-26 13:41:58.380272');
INSERT INTO `django_migrations` VALUES (21, 'testsys', '0001_initial', '2025-06-26 13:41:58.460933');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('x41kolczs5l3xt4lvbffr54kq2hw0a1f', '.eJzNVsuu0zAQ_ZUq6z6c2M7jLtmzZEWuKj8mrSEPsBMhdNV_x04q6DVuE0rRZRNLnpMzM-eMnbxEezb0x_1gQO-VjJ6iOFpf7nEmPkPrAvITaw_dVnRtrxXfOsj2HDXb952E-t0Z-4rgyMzRvs2IQMCzAuEUxxViFCNaZRWvuMxISgteFZwKJIDxuMCJQBSTCktGaYEgybEjbaAdjOX6-FJGLWugjJ5WZVSWA8WU2iXnQtol4yx2C0FpGa0tQtmaJ2zF9KpiG6G0qGEKNq5y48I3aeeJBl1PsR2TjWp33zotzfjcTQAm5YfrGBs947gGJoUeGj5f1p90e1qv7u_w9OzCoKSLxgglAbYiL3JXSgpwt15fBzC96to5zX7i3kS35Z36umF_Iw7Qp5LwsVJJHznPr2nTFIGjBbGE1nert_Kb72ZcJfRM1dcdC2CXu3avFrOyLu_ft4zOcuecIzdxlZ24v9NWg7h5gwSw_4G2y_v3tU39DRJIltHEHb80wdkjz8clbZjIfdHCnrmIGZ_XvbrALPfo3l5nZLvVn29B7m9kAfKcMzLdrq5ASnLhUuF8zJgR_HtG4zKao4Jabljd_1N73P_IjDu_IMvNeUDTj_MpRiEuEORKFeM4bkR3uCHZQXfDlxnNJsybi7aoUV-y2B_t4vQcnX4A5hl01A:1uVqtV:FQsgXAbMHgQitzma4i2U8uN-Vu8e7QTOkVIkyultWPU', '2025-07-13 12:12:25.471178');

-- ----------------------------
-- Table structure for testsys_testdetail
-- ----------------------------
DROP TABLE IF EXISTS `testsys_testdetail`;
CREATE TABLE `testsys_testdetail`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_answer` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_correct` tinyint(1) NOT NULL,
  `question_id` bigint NOT NULL,
  `record_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `testsys_testdetail_question_id_e4bfab32_fk_words_question_id`(`question_id` ASC) USING BTREE,
  INDEX `testsys_testdetail_record_id_81ad90d3_fk_testsys_testrecord_id`(`record_id` ASC) USING BTREE,
  CONSTRAINT `testsys_testdetail_question_id_e4bfab32_fk_words_question_id` FOREIGN KEY (`question_id`) REFERENCES `words_question` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `testsys_testdetail_record_id_81ad90d3_fk_testsys_testrecord_id` FOREIGN KEY (`record_id`) REFERENCES `testsys_testrecord` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 63 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of testsys_testdetail
-- ----------------------------
INSERT INTO `testsys_testdetail` VALUES (1, 'A', 1, 1, 1);
INSERT INTO `testsys_testdetail` VALUES (2, 'B', 1, 2, 1);
INSERT INTO `testsys_testdetail` VALUES (3, 'D', 0, 3, 1);
INSERT INTO `testsys_testdetail` VALUES (4, 'A', 1, 4, 2);
INSERT INTO `testsys_testdetail` VALUES (5, 'C', 0, 2, 2);
INSERT INTO `testsys_testdetail` VALUES (6, 'A', 1, 1, 3);
INSERT INTO `testsys_testdetail` VALUES (7, 'A', 1, 4, 3);
INSERT INTO `testsys_testdetail` VALUES (8, 'A', 0, 42, 4);
INSERT INTO `testsys_testdetail` VALUES (9, 'A', 0, 31, 4);
INSERT INTO `testsys_testdetail` VALUES (10, 'A', 0, 45, 4);
INSERT INTO `testsys_testdetail` VALUES (11, 'A', 1, 39, 4);
INSERT INTO `testsys_testdetail` VALUES (12, 'A', 0, 40, 4);
INSERT INTO `testsys_testdetail` VALUES (13, 'A', 1, 44, 4);
INSERT INTO `testsys_testdetail` VALUES (14, 'A', 0, 43, 4);
INSERT INTO `testsys_testdetail` VALUES (15, 'A', 1, 46, 4);
INSERT INTO `testsys_testdetail` VALUES (16, 'A', 0, 38, 4);
INSERT INTO `testsys_testdetail` VALUES (17, 'A', 0, 41, 4);
INSERT INTO `testsys_testdetail` VALUES (18, 'A', 0, 41, 5);
INSERT INTO `testsys_testdetail` VALUES (19, 'A', 1, 39, 5);
INSERT INTO `testsys_testdetail` VALUES (20, 'A', 0, 38, 5);
INSERT INTO `testsys_testdetail` VALUES (21, 'A', 0, 31, 5);
INSERT INTO `testsys_testdetail` VALUES (22, 'A', 0, 43, 5);
INSERT INTO `testsys_testdetail` VALUES (23, 'A', 0, 40, 5);
INSERT INTO `testsys_testdetail` VALUES (24, 'A', 1, 46, 5);
INSERT INTO `testsys_testdetail` VALUES (25, 'A', 0, 42, 5);
INSERT INTO `testsys_testdetail` VALUES (26, 'A', 0, 45, 5);
INSERT INTO `testsys_testdetail` VALUES (27, 'A', 1, 44, 5);
INSERT INTO `testsys_testdetail` VALUES (28, 'A', 0, 38, 6);
INSERT INTO `testsys_testdetail` VALUES (29, 'A', 0, 41, 6);
INSERT INTO `testsys_testdetail` VALUES (30, 'A', 0, 42, 6);
INSERT INTO `testsys_testdetail` VALUES (31, 'A', 1, 46, 6);
INSERT INTO `testsys_testdetail` VALUES (32, 'A', 0, 37, 6);
INSERT INTO `testsys_testdetail` VALUES (33, 'A', 1, 39, 6);
INSERT INTO `testsys_testdetail` VALUES (34, 'A', 0, 43, 6);
INSERT INTO `testsys_testdetail` VALUES (35, 'A', 0, 45, 6);
INSERT INTO `testsys_testdetail` VALUES (36, 'A', 1, 44, 6);
INSERT INTO `testsys_testdetail` VALUES (37, 'A', 0, 40, 6);
INSERT INTO `testsys_testdetail` VALUES (38, '\0', 0, 41, 7);
INSERT INTO `testsys_testdetail` VALUES (39, '\0', 0, 45, 7);
INSERT INTO `testsys_testdetail` VALUES (40, '\0', 0, 39, 7);
INSERT INTO `testsys_testdetail` VALUES (41, '\0', 0, 44, 7);
INSERT INTO `testsys_testdetail` VALUES (42, '\0', 0, 46, 7);
INSERT INTO `testsys_testdetail` VALUES (43, 'A', 0, 45, 8);
INSERT INTO `testsys_testdetail` VALUES (44, 'B', 1, 41, 8);
INSERT INTO `testsys_testdetail` VALUES (45, 'C', 1, 38, 8);
INSERT INTO `testsys_testdetail` VALUES (46, 'C', 1, 43, 8);
INSERT INTO `testsys_testdetail` VALUES (47, 'A', 1, 46, 8);
INSERT INTO `testsys_testdetail` VALUES (48, 'C', 1, 43, 9);
INSERT INTO `testsys_testdetail` VALUES (49, 'A', 0, 37, 9);
INSERT INTO `testsys_testdetail` VALUES (50, 'C', 1, 38, 9);
INSERT INTO `testsys_testdetail` VALUES (51, 'C', 1, 31, 9);
INSERT INTO `testsys_testdetail` VALUES (52, 'B', 1, 41, 9);
INSERT INTO `testsys_testdetail` VALUES (53, 'C', 1, 38, 10);
INSERT INTO `testsys_testdetail` VALUES (54, 'C', 1, 43, 10);
INSERT INTO `testsys_testdetail` VALUES (55, 'A', 1, 39, 10);
INSERT INTO `testsys_testdetail` VALUES (56, 'A', 0, 45, 10);
INSERT INTO `testsys_testdetail` VALUES (57, 'A', 0, 42, 10);
INSERT INTO `testsys_testdetail` VALUES (58, 'B', 0, 31, 11);
INSERT INTO `testsys_testdetail` VALUES (59, 'A', 1, 39, 11);
INSERT INTO `testsys_testdetail` VALUES (60, 'B', 0, 45, 11);
INSERT INTO `testsys_testdetail` VALUES (61, 'B', 0, 44, 11);
INSERT INTO `testsys_testdetail` VALUES (62, 'B', 1, 37, 11);

-- ----------------------------
-- Table structure for testsys_testrecord
-- ----------------------------
DROP TABLE IF EXISTS `testsys_testrecord`;
CREATE TABLE `testsys_testrecord`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `score` int NOT NULL,
  `vocab_estimate` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `testsys_testrecord_user_id_c18981cc_fk_users_user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `testsys_testrecord_user_id_c18981cc_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of testsys_testrecord
-- ----------------------------
INSERT INTO `testsys_testrecord` VALUES (1, 90, 5000, '2025-06-26 13:57:27.125933', 1);
INSERT INTO `testsys_testrecord` VALUES (2, 80, 4000, '2025-06-26 13:57:27.130600', 2);
INSERT INTO `testsys_testrecord` VALUES (3, 90, 5000, '2025-06-26 13:57:51.650167', 1);
INSERT INTO `testsys_testrecord` VALUES (4, 90, 5000, '2025-06-29 07:28:36.708289', 1);
INSERT INTO `testsys_testrecord` VALUES (5, 90, 5000, '2025-06-29 13:14:36.066337', 1);
INSERT INTO `testsys_testrecord` VALUES (6, 90, 5000, '2025-06-29 13:30:57.554418', 1);
INSERT INTO `testsys_testrecord` VALUES (7, 0, 2000, '2025-06-29 13:36:12.688860', 7);
INSERT INTO `testsys_testrecord` VALUES (8, 80, 10000, '2025-06-29 13:43:04.002916', 10);
INSERT INTO `testsys_testrecord` VALUES (9, 80, 10000, '2025-06-29 13:57:36.650421', 11);
INSERT INTO `testsys_testrecord` VALUES (10, 60, 7000, '2025-06-29 14:02:54.619891', 12);
INSERT INTO `testsys_testrecord` VALUES (11, 40, 5000, '2025-06-29 14:05:15.280531', 1);

-- ----------------------------
-- Table structure for users_user
-- ----------------------------
DROP TABLE IF EXISTS `users_user`;
CREATE TABLE `users_user`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `openid` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nickname` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `avatar` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `openid`(`openid` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users_user
-- ----------------------------
INSERT INTO `users_user` VALUES (1, 'test_openid_001', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-26 13:45:48.383299');
INSERT INTO `users_user` VALUES (2, 'test_openid_002', '测试用户2', 'https://example.com/avatar2.png', '2025-06-26 13:57:27.106910');
INSERT INTO `users_user` VALUES (3, 'test_openid_1751203446605', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:24:06.699640');
INSERT INTO `users_user` VALUES (4, 'test_openid_1751203577888', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:26:17.982222');
INSERT INTO `users_user` VALUES (5, 'test_openid_1751203673676', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:27:53.761608');
INSERT INTO `users_user` VALUES (6, 'test_openid_1751203701076', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:28:21.168722');
INSERT INTO `users_user` VALUES (7, 'test_openid_1751204140562', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:35:40.676805');
INSERT INTO `users_user` VALUES (8, 'test_openid_1751204333753', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:38:53.848396');
INSERT INTO `users_user` VALUES (9, 'test_openid_1751204520108', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:42:00.193711');
INSERT INTO `users_user` VALUES (10, 'test_openid_1751204558187', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:42:38.277330');
INSERT INTO `users_user` VALUES (11, 'test_openid_1751205379509', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 13:56:19.659866');
INSERT INTO `users_user` VALUES (12, 'test_openid_1751205750381', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 14:02:30.475927');
INSERT INTO `users_user` VALUES (13, 'test_openid_1751205794711', '测试用户', 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', '2025-06-29 14:03:15.277659');

-- ----------------------------
-- Table structure for words_question
-- ----------------------------
DROP TABLE IF EXISTS `words_question`;
CREATE TABLE `words_question`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `options` json NOT NULL,
  `answer` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `type` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `word_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `words_question_word_id_c470f01d_fk_words_word_id`(`word_id` ASC) USING BTREE,
  CONSTRAINT `words_question_word_id_c470f01d_fk_words_word_id` FOREIGN KEY (`word_id`) REFERENCES `words_word` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 57 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of words_question
-- ----------------------------
INSERT INTO `words_question` VALUES (1, '{\"A\": \"苹果\", \"B\": \"香蕉\", \"C\": \"橙子\", \"D\": \"葡萄\"}', 'A', 'choice', 1);
INSERT INTO `words_question` VALUES (2, '{\"A\": \"苹果\", \"B\": \"香蕉\", \"C\": \"橙子\", \"D\": \"葡萄\"}', 'B', 'choice', 2);
INSERT INTO `words_question` VALUES (3, '{\"A\": \"苹果\", \"B\": \"香蕉\", \"C\": \"橙子\", \"D\": \"葡萄\"}', 'C', 'choice', 3);
INSERT INTO `words_question` VALUES (4, '{\"A\": \"梨\", \"B\": \"苹果\", \"C\": \"香蕉\", \"D\": \"葡萄\"}', 'A', 'choice', 5);
INSERT INTO `words_question` VALUES (31, '{\"A\": \"快\", \"B\": \"水\", \"C\": \"葡萄\", \"D\": \"兴奋\"}', 'C', 'choice', 4);
INSERT INTO `words_question` VALUES (32, '{\"A\": \"困难的\", \"B\": \"汽车\", \"C\": \"书\", \"D\": \"满足\"}', 'C', 'choice', 6);
INSERT INTO `words_question` VALUES (33, '{\"A\": \"绿色\", \"B\": \"牛\", \"C\": \"钢笔\", \"D\": \"橙色\"}', 'C', 'choice', 7);
INSERT INTO `words_question` VALUES (34, '{\"A\": \"香蕉\", \"B\": \"橙子\", \"C\": \"汽车\", \"D\": \"可能的\"}', 'C', 'choice', 8);
INSERT INTO `words_question` VALUES (35, '{\"A\": \"房子\", \"B\": \"完成\", \"C\": \"低\", \"D\": \"高\"}', 'A', 'choice', 9);
INSERT INTO `words_question` VALUES (36, '{\"A\": \"水\", \"B\": \"月亮\", \"C\": \"鱼\", \"D\": \"山\"}', 'A', 'choice', 10);
INSERT INTO `words_question` VALUES (37, '{\"A\": \"好\", \"B\": \"美丽的\", \"C\": \"真实的\", \"D\": \"粉色\"}', 'B', 'choice', 11);
INSERT INTO `words_question` VALUES (38, '{\"A\": \"工作\", \"B\": \"好\", \"C\": \"重要的\", \"D\": \"汽车\"}', 'C', 'choice', 12);
INSERT INTO `words_question` VALUES (39, '{\"A\": \"困难的\", \"B\": \"猫\", \"C\": \"精彩的\", \"D\": \"高\"}', 'A', 'choice', 13);
INSERT INTO `words_question` VALUES (40, '{\"A\": \"高\", \"B\": \"窗户\", \"C\": \"坏\", \"D\": \"有趣的\"}', 'D', 'choice', 14);
INSERT INTO `words_question` VALUES (41, '{\"A\": \"电脑\", \"B\": \"必要的\", \"C\": \"手机\", \"D\": \"疲惫\"}', 'B', 'choice', 15);
INSERT INTO `words_question` VALUES (42, '{\"A\": \"全面的\", \"B\": \"可能的\", \"C\": \"山\", \"D\": \"雄辩的\"}', 'B', 'choice', 16);
INSERT INTO `words_question` VALUES (43, '{\"A\": \"天空\", \"B\": \"星星\", \"C\": \"不同的\", \"D\": \"火\"}', 'C', 'choice', 17);
INSERT INTO `words_question` VALUES (44, '{\"A\": \"成功的\", \"B\": \"努力\", \"C\": \"休息\", \"D\": \"星星\"}', 'A', 'choice', 18);
INSERT INTO `words_question` VALUES (45, '{\"A\": \"有趣的\", \"B\": \"困难的\", \"C\": \"失望\", \"D\": \"精彩的\"}', 'D', 'choice', 19);
INSERT INTO `words_question` VALUES (46, '{\"A\": \"危险的\", \"B\": \"紧张\", \"C\": \"桌子\", \"D\": \"精彩的\"}', 'A', 'choice', 20);
INSERT INTO `words_question` VALUES (47, '{\"A\": \"绿色\", \"B\": \"羊\", \"C\": \"写作\", \"D\": \"完成\"}', 'D', 'choice', 21);
INSERT INTO `words_question` VALUES (48, '{\"A\": \"阅读\", \"B\": \"努力\", \"C\": \"成功的\", \"D\": \"雄辩的\"}', 'B', 'choice', 22);
INSERT INTO `words_question` VALUES (49, '{\"A\": \"牛\", \"B\": \"房子\", \"C\": \"满足\", \"D\": \"坚持\"}', 'D', 'choice', 23);
INSERT INTO `words_question` VALUES (50, '{\"A\": \"马\", \"B\": \"可能的\", \"C\": \"重要的\", \"D\": \"有韧性的\"}', 'D', 'choice', 24);
INSERT INTO `words_question` VALUES (51, '{\"A\": \"深刻的\", \"B\": \"草\", \"C\": \"月亮\", \"D\": \"雨\"}', 'A', 'choice', 25);
INSERT INTO `words_question` VALUES (52, '{\"A\": \"钢笔\", \"B\": \"房子\", \"C\": \"鸟\", \"D\": \"雄辩的\"}', 'D', 'choice', 26);
INSERT INTO `words_question` VALUES (53, '{\"A\": \"复杂的\", \"B\": \"真实的\", \"C\": \"橙子\", \"D\": \"重要的\"}', 'B', 'choice', 27);
INSERT INTO `words_question` VALUES (54, '{\"A\": \"创新的\", \"B\": \"困难的\", \"C\": \"美丽的\", \"D\": \"小\"}', 'A', 'choice', 28);
INSERT INTO `words_question` VALUES (55, '{\"A\": \"复杂的\", \"B\": \"有趣的\", \"C\": \"椅子\", \"D\": \"绿色\"}', 'A', 'choice', 29);
INSERT INTO `words_question` VALUES (56, '{\"A\": \"窗户\", \"B\": \"全面的\", \"C\": \"香蕉\", \"D\": \"鸭\"}', 'B', 'choice', 30);

-- ----------------------------
-- Table structure for words_word
-- ----------------------------
DROP TABLE IF EXISTS `words_word`;
CREATE TABLE `words_word`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `word` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `meaning` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `level` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `difficulty` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of words_word
-- ----------------------------
INSERT INTO `words_word` VALUES (1, 'apple', '苹果', 'CET4', 1);
INSERT INTO `words_word` VALUES (2, 'banana', '香蕉', 'CET4', 1);
INSERT INTO `words_word` VALUES (3, 'orange', '橙子', 'CET4', 1);
INSERT INTO `words_word` VALUES (4, 'grape', '葡萄', 'CET4', 2);
INSERT INTO `words_word` VALUES (5, 'pear', '梨', 'CET4', 1);
INSERT INTO `words_word` VALUES (6, 'book', '书', 'CET4', 1);
INSERT INTO `words_word` VALUES (7, 'pen', '钢笔', 'CET4', 1);
INSERT INTO `words_word` VALUES (8, 'car', '汽车', 'CET4', 1);
INSERT INTO `words_word` VALUES (9, 'house', '房子', 'CET4', 1);
INSERT INTO `words_word` VALUES (10, 'water', '水', 'CET4', 1);
INSERT INTO `words_word` VALUES (11, 'beautiful', '美丽的', 'CET6', 2);
INSERT INTO `words_word` VALUES (12, 'important', '重要的', 'CET6', 2);
INSERT INTO `words_word` VALUES (13, 'difficult', '困难的', 'CET6', 2);
INSERT INTO `words_word` VALUES (14, 'interesting', '有趣的', 'CET6', 2);
INSERT INTO `words_word` VALUES (15, 'necessary', '必要的', 'CET6', 2);
INSERT INTO `words_word` VALUES (16, 'possible', '可能的', 'CET6', 2);
INSERT INTO `words_word` VALUES (17, 'different', '不同的', 'CET6', 2);
INSERT INTO `words_word` VALUES (18, 'successful', '成功的', 'CET6', 2);
INSERT INTO `words_word` VALUES (19, 'wonderful', '精彩的', 'CET6', 2);
INSERT INTO `words_word` VALUES (20, 'dangerous', '危险的', 'CET6', 2);
INSERT INTO `words_word` VALUES (21, 'accomplish', '完成', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (22, 'endeavor', '努力', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (23, 'persevere', '坚持', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (24, 'resilient', '有韧性的', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (25, 'profound', '深刻的', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (26, 'eloquent', '雄辩的', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (27, 'authentic', '真实的', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (28, 'innovative', '创新的', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (29, 'sophisticated', '复杂的', 'TOEFL', 3);
INSERT INTO `words_word` VALUES (30, 'comprehensive', '全面的', 'TOEFL', 3);

SET FOREIGN_KEY_CHECKS = 1;
