-- Module 3: list all bands with GLAM as their main style

SELECT band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS 'lifespan'
FROM metal_bands
GROUP BY band_name
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
