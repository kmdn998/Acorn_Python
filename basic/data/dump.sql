BEGIN TRANSACTION;
CREATE TABLE phonebook(name varchar(10), phonenum text);
INSERT INTO "phonebook" VALUES('tom','010-1234-1234');
INSERT INTO "phonebook" VALUES('been','010-4567-4567');
INSERT INTO "phonebook" VALUES('na','010-5678-4567');
INSERT INTO "phonebook" VALUES('jane','010-111-111');
INSERT INTO "phonebook" VALUES('jerry','010-222-222');
INSERT INTO "phonebook" VALUES('marry','010-333-333');
COMMIT;
