SELECT * FROM Apartments
WHERE price > ( SELECT AVG(price)FROM Apartments) and status in ('Not rented')
ORDER BY price;