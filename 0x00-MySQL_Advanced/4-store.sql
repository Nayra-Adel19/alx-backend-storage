-- Quantity in the table items can be negative

CREATE TRIGGER  decreas_quantity 
AFTER INSERT ON orders
FOR EACH ROW UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
