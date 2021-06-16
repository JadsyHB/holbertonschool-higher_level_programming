-- Module 4: Trigger

CREATE TRIGGER `MyTrigger` 
    AFTER INSERT INTO orders
    FOR EACH ROW
    BEGIN
      UPDATE ITEMS
           SET quantity = quantity-1
    END;
