SELECT MaritalStatus, round(AVG(Age)) AS AverageAge
FROM Customer
GROUP BY MaritalStatus;

SELECT 
    CASE 
        WHEN gender = 0 THEN 'Wanita'
        WHEN gender = 1 THEN 'Pria'
    END AS GenderType,
    round(AVG(age)) AS AverageAge
FROM customer
GROUP BY gender;

SELECT s.storename, SUM(t.qty) AS TotalQuantity
FROM store s
JOIN transaction t ON s.storeid = t.storeid
GROUP BY s.storename
ORDER BY totalquantity DESC
LIMIT 1;

SELECT p.productname, SUM(t.totalamount) AS TotalAmount
FROM product p
JOIN transaction t ON p.productid = t.productid
GROUP BY p.productname
ORDER BY TotalAmount DESC
LIMIT 1;