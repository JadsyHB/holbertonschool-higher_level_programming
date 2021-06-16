-- Module 5: email

CREATE TRIGGER validater BEFORE UPDATE ON users
FOR EACH ROW
IF OLD.email <> NEW.email THEN
SET NEW.valid_email = 0 END IF;
