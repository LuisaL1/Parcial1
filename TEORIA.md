## SECCIÓN TEÓRICA
**SM-1**
Un equipo de desarrollo termina de escribir toda la funcionalidad de un módulo y luego le pide al QA que diseñe las pruebas. Según lo visto en clase, ¿cómo se llama este enfoque y cuál es su principal problema?

C. 

**SM-2**
Un desarrollador escribe el siguiente ciclo: primero implementa la función `calcular_descuento()` completa con todos los casos que se le ocurren, luego escribe los tests para verificar que funciona. ¿Qué regla de TDD está violando?

B.

**PREGUNTAS ABIERTAS**
**PA-1**
En TDD, el GREEN obliga a escribir el código más simple posible porque el objetivo en ese momento no es diseñar la solución perfecta, sino únicamente hacer pasar el test que acaba de fallar implementando las funcionalidades básicas que aborden la necesidad que se requiere sin agregar lógica innecesaria. El refactor y la limpieza vienen después, cuando ya existe seguridad gracias a las pruebas automatizadas
**PA-2**
TDD está orientado principalmente a los desarrolladores (parte técnica) y se enfoca en construir código correcto desde el inicio. Su objetivo es garantizar que cada unidad del sistema funcione correctamente y que el diseño del código evolucione de manera segura. BDD busca mejorar la comunicación entre negocio, QA y desarrollo usando escenarios escritos en lenguaje entendible para todos 
**PA-3**
Tener alta cobertura de código no significa que el sistema esté libre de errores. La cobertura solo indica cuánto código fue ejecutado durante las pruebas, pero no nos garantiza que los resultados verificados sean correctos. Por ejemplo, un método podría calcular descuentos incorrectamente y aun así tener 100% de cobertura si los tests solo verifican que la función se ejecute sin errores. También puede ocurrir que un test pase porque no valida el resultado esperado con suficiente precisión. Un sistema puede recorrer todas las líneas de código y seguir teniendo defectos de lógica, reglas de negocio mal implementadas o casos borde no considerados
**PA-4**
La lógica de probar únicamente el 20% es incorrecta porque los errores suelen aparecer en los límites del rango permitido, no en los valores intermedios. En la regla del descuento, el rango válido es entre 0% y 40%, así que es importante probar valores límite y cercanos a ellos. Yo probaría 0% y 40% porque son los extremos válidos, además de valores inválidos como -1% y 41% para verificar que el sistema rechace correctamente entradas fuera del rango. También probaría valores cercanos como 1% y 39% para asegurar que no existan errores de comparación en las validaciones

**PA-5**
Las prácticas de TDD y BDD se conectan directamente con CI/CD porque proporcionan una suite automatizada de pruebas que puede ejecutarse continuamente en el pipeline. En integración continua, cada cambio que sube un desarrollador debe validarse automáticamente para detectar errores rápido mientras que el  TDD aporta pruebas unitarias confiables y BDD aporta validación del comportamiento esperado por el negocio. Si el equipo no tiene una suite sólida de tests automatizados, el pipeline de CI/CD pierde valor porque no puede garantizar que los cambios nuevos no rompan funcionalidades existentes. En este caso, el despliegue continuo se vuelve riesgoso y aumentan los errores en producción