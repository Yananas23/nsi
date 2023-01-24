SELECT categorie FROM evolution ORDER BY categorie ASC;
SELECT COUNT(DISTINCT categorie) AS NbLigne FROM evolution;
SELECT code FROM ville WHERE nom='Caullery';
SELECT * FROM evolution WHERE code='59140';
SELECT code FROM evolution WHERE effectif>='2000';
SELECT SUM(effectif) FROM evolution WHERE genre='Femmes' and categorie='Agriculteurs Exploitants';
SELECT AVG(effectif) FROM evolution WHERE NOT categorie='Retraités';
