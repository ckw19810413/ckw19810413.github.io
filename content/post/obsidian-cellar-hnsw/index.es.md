---
title: "Fábula diaria de conceptos de posgrado: Small World navegable y jerárquico (HNSW)"
description: "A través de la historia de una bodega de obsidiana y unas arañas guía, esta fábula explica de forma intuitiva HNSW, el algoritmo de búsqueda de alta eficiencia que está en el núcleo de las bases de datos vectoriales."
slug: "obsidian-cellar-hnsw"
layout: "single"
summary: "Esta fábula narra la dificultad de los eruditos para encontrar piedras de concepto en una bodega de obsidiana, y cómo un arquitecto ciego resuelve el problema construyendo una telaraña tridimensional con arañas guía: una metáfora perfecta del algoritmo HNSW (Hierarchical Navigable Small World) usado en las bases de datos vectoriales."
publishDate: 2026-08-18
updatedDate: 2026-08-18
categories:
  - "Conceptos de IA Explicados"
  - "Grandes Modelos de Lenguaje"
tags:
  - "HNSW"
  - "Base de Datos Vectorial"
  - "Vector Database"
  - "RAG"
  - "Búsqueda con IA"
draft: false
---

¡Buenas noches! Aquí tienes la "Fábula diaria de conceptos de posgrado" de hoy.

## La bodega de obsidiana y las arañas guía

En lo más profundo del continente del conocimiento se halla una enorme biblioteca subterránea conocida como la "Bodega de Obsidiana". No guarda libros de papel; en su lugar, flotan en ella decenas de millones de "piedras de concepto" que emiten un tenue resplandor. Cada piedra sella un pasaje de texto o una sola idea.

La bodega tiene una regla peculiar: cuanto más cercanas en significado son dos piedras de concepto, más próximas se sitúan en el espacio.

Cada día los eruditos acuden a la bodega portando una "piedra desconocida", tratando de encontrar el puñado de piedras de la bodega más similares a ella.

Al principio, los eruditos empleaban una "búsqueda de peinado". Con la piedra desconocida en la mano, caminaban hasta la primera piedra de concepto para compararla, luego hasta la segunda, la tercera… Cuando el número de piedras alcanzaba las decenas de millones, encontrar una sola podía llevar buena parte de una vida, y muchos eruditos caían muertos de agotamiento en la bodega.

Más tarde, un artesano ingenioso inventó el "método del hilado". Con seda de araña ató entre sí las piedras que estaban próximas, formando una enorme telaraña tridimensional.

Ahora el erudito solo tenía que elegir cualquier piedra al azar como punto de partida, mirar a sus vecinos conectados por seda de araña, escoger el más cercano al objetivo y caminar hacia él; después mirar a los nuevos vecinos y volver a caminar. Era como tirar del bejuco para hallar la calabaza: hasta que en los alrededores no quedara ninguna piedra más cercana.

¡Este método era mucho más rápido! Pero tenía dos defectos fatales:
Primero, si el punto de partida elegido estaba demasiado lejos del objetivo, el erudito tenía que gatear por la red durante muchísimo tiempo.
Segundo, a veces el erudito se metía en un "callejón sin salida": todas las piedras de alrededor parecían ser las más cercanas, pero la respuesta verdaderamente perfecta estaba en realidad oculta en el otro extremo de la red, sin ninguna seda de araña que uniera ambos puntos.

Justo cuando la bodega estaba a punto de colapsar, un arquitecto ciego llegó con un grupo de mágicas "arañas guía". El arquitecto ciego no alteró los decenas de millones de piedras del nivel inferior, pero hizo que las arañas guía construyeran, por encima de la bodega original, varias capas de "red suspendida".

* **La capa superior (la capa de la nube):** Las arañas eligieron solo una fracción ínfima de las piedras de la bodega (alrededor de una de cada diez mil) como "hitos intercontinentales", las subieron a la capa más alta y las conectaron con seda de araña larguísima.
* **La capa intermedia (la capa de la ciudad):** Una capa más abajo, las arañas eligieron el uno por ciento de las piedras como "hitos urbanos" y las conectaron.
* **La capa inferior (la capa del suelo):** Mantuvo la densa red original en la que todas las decenas de millones de piedras estaban interconectadas.

Ahora, cuando un erudito llega con una piedra desconocida para buscar, la búsqueda del tesoro se vuelve exquisitamente elegante:

Toma el ascensor directo a la capa superior. Aquí solo hay unos pocos "hitos intercontinentales", y de un vistazo distingue qué hito está más cerca de su objetivo. Da un paso gigantesco y se sitúa sobre ese hito.

A continuación, salta por la trampilla del hito a la capa de abajo, la "capa de la ciudad". Aquí hay más piedras, pero no necesita buscar desde cero, pues ya ha aterrizado en la región intercontinental correcta. Siguiendo la seda de araña de la capa de la ciudad, camina unos pasos hasta el hito urbano más cercano.

Por último, desciende del todo hasta la capa inferior. A estas alturas está de pie, con precisión, en la puerta de la casa de la piedra objetivo. Solo tiene que dar dos o tres pasos por la densa capa del suelo para encontrar la única piedra de concepto más perfecta.

La telaraña tridimensional del arquitecto ciego convirtió una búsqueda que antes requería diez millones de comparaciones en un viaje impecable de apenas unas decenas de saltos ligeros entre distintas plantas.

## La revelación: Small World navegable y jerárquico (HNSW)

Lo que describe esta historia es un algoritmo de nivel de posgrado, central y de alta eficiencia, de los campos de la inteligencia artificial moderna, las bases de datos vectoriales (Vector Database) y la generación aumentada por recuperación en grandes modelos (RAG): el **Small World navegable y jerárquico (Hierarchical Navigable Small World, abreviado HNSW)**.

Cuando construimos una enorme base de conocimiento en local y convertimos el texto en vectores de alta dimensión (por ejemplo, embeddings generados con nomic-embed-text), encontrar a gran velocidad los pasajes más similares a la pregunta de un usuario entre un enorme montón de vectores de alta dimensión es un desafío mayúsculo.

El K-Nearest Neighbors (KNN) tradicional requiere calcular la distancia a cada uno de los vectores, con una complejidad temporal de $O(N)$, algo inaceptable al manejar datos a escala de millones. HNSW, al construir una estructura de grafo multinivel, combina con ingenio la idea de la **lista de saltos (Skip List)** con las propiedades de la **red de mundo pequeño (Small World Network)**.

Permite que el algoritmo realice una "localización aproximada" de gran zancada al inicio de la búsqueda y un "ajuste fino" de corto alcance en la fase final, logrando comprimir drásticamente la complejidad temporal de la búsqueda de vectores de alta dimensión hasta cerca de $O(\log N)$.

## Correspondencia de la metáfora

| Elemento de la historia | Concepto de algoritmo y sistema | Explicación |
|---|---|---|
| **La bodega de obsidiana y las piedras de concepto** | Base de datos vectorial y embeddings de texto (Vector DB & Text Embeddings) | Convertir conocimiento, documentos o notas en puntos de coordenadas en el espacio. Cuanto más cercanos en significado son dos textos, menor es su distancia en el espacio multidimensional. |
| **La búsqueda de peinado** | Búsqueda por fuerza bruta (Brute-force Search / Exact KNN) | Calcular una por una la distancia entre el vector de consulta y todos los vectores de la base de datos (por ejemplo, la similitud del coseno): extremadamente lento. |
| **El método del hilado plano** | Grafo de mundo pequeño navegable (Navigable Small World, NSW) | Conectar solo nodos adyacentes en un único plano. Propenso a quedar atrapado en un óptimo local (un callejón sin salida) e ineficiente cuando el punto de partida está lejos del objetivo. |
| **Las plantas de la red suspendida (nube, ciudad, suelo)** | Las capas jerárquicas de HNSW (Hierarchical Layers) | El núcleo del algoritmo HNSW. La capa 0 contiene todos los nodos; cuanto más alta es la capa, menos nodos hay, decreciendo de forma exponencial. |
| **Los hitos intercontinentales de la cima** | Puntos de entrada en las capas superiores (Entry Points in Top Layers) | En las capas de grafo más dispersas, aportan capacidad de salto de larga distancia, garantizando que el algoritmo se aproxime rápido a la región global donde se halla el objetivo. |
| **Descender capa a capa buscando** | Enrutamiento por búsqueda voraz (Greedy Search Routing) | El algoritmo empieza en la capa más alta; tras hallar el nodo más cercano en esa capa, lo pasa hacia abajo como punto de partida de la siguiente, hasta llegar a la capa 0 y encontrar los vecinos más cercanos finales (Nearest Neighbors). |
