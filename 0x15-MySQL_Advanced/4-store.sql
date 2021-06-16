-- Module 4: Trigger

CREATE TRIGGER `MyTrigger` 
    AFTER INSERT on orders
    FOR EACH ROW
    UPDATE items SET quantity = quantity-NEW.number
    WHERE name = NEW.item_name;
