-- Module 3: list all bands with GLAM as their main style

SELECT band_name, (IFNULL(split, 2020) - formed) AS 'lifespan'
FROM metal_bands
GROUP BY band_name
ORDER BY lifespan DESC;
