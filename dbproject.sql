--
-- File generated with SQLiteStudio v3.2.1 on Fri Dec 10 16:20:26 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Penyakit
CREATE TABLE Penyakit (id_penyakit STRING PRIMARY KEY NOT NULL, posisi STRING NOT NULL, kondisi STRING NOT NULL, diagnosa STRING NOT NULL);
INSERT INTO Penyakit (id_penyakit, posisi, kondisi, diagnosa) VALUES (1, 'Kepala', 'Bengkak', 'Sakit Kepala Kluster');
INSERT INTO Penyakit (id_penyakit, posisi, kondisi, diagnosa) VALUES (2, 'Kepala', 'Nyeri', 'Sakit Kepala, ada indikasi Darah Tinggi');
INSERT INTO Penyakit (id_penyakit, posisi, kondisi, diagnosa) VALUES (3, 'Dada', 'Bengkak', 'Peradangan Tulang, ada indikasi Jantung Bengkak');
INSERT INTO Penyakit (id_penyakit, posisi, kondisi, diagnosa) VALUES (4, 'Dada', 'Nyeri', 'Serangan Jantung, Angin Duduk');
INSERT INTO Penyakit (id_penyakit, posisi, kondisi, diagnosa) VALUES (5, 'Kaki', 'Bengkak', 'Cedera/Terkilir, Kaki Gajah');
INSERT INTO Penyakit (id_penyakit, posisi, kondisi, diagnosa) VALUES (6, 'Kaki', 'Nyeri', 'Cedera/Terkilir, Asam Urat, Peradangan Jaringan');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
