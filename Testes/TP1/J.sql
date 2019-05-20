DROP FUNCTION IF EXISTS validateCustomer;
DELIMITER $

CREATE FUNCTION validateCustomer(customer_id INT)
RETURNS TEXT
BEGIN
  DECLARE result TEXT;
  IF customer_id NOT IN (select CustomerId from CUSTOMER) THEN
    SET result = 'DOES NOT EXIST';
  ELSE IF (SELECT Active from CUSTOMER WHERE CustomerId=customer_id) = FALSE  THEN
    IF 1<= (SELECT COUNT(*) FROM STREAM WHERE CustomerId=customer_id AND YEAR(StreamDate)>=2018) THEN
      SET result = 'ACTIVE';
    ELSE
      SET result = 'OK';
    END IF;
  ELSE IF (SELECT Active from CUSTOMER WHERE CustomerId=customer_id)=TRUE THEN
    IF 0= (SELECT COUNT(*) FROM STREAM WHERE CustomerId=customer_id AND YEAR(StreamDate)>=2018) THEN
      SET result = 'DEACTIVE';
    ELSE
      SET result = 'OK';
    END IF;
  ELSE 
    SET result = 'OK';
  END IF;
  RETURN result;
END$
DELIMITER ;