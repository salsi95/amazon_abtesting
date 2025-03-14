# Proyecto AB testing Amazon
## 1. **Contexto y Problema Actual**

Amazon, reconocido líder global en comercio electrónico, se enfrenta al desafío de integrar y aprovechar de manera óptima la vasta cantidad de datos generados en su plataforma. A pesar de contar con una infraestructura robusta, se ha identificado que existen oportunidades para mejorar la **personalización de la experiencia de compra**, **incrementar la tasa de conversión** y **optimizar las campañas de marketing**. Actualmente, la información sobre las ventas, el comportamiento del usuario y las variables relacionadas con la compra se encuentran dispersas en múltiples fuentes, lo que dificulta la obtención de insights accionables que permitan responder rápidamente a las tendencias del mercado y a las necesidades de los clientes.

Con el objetivo de abordar estos problemas, se ha decidido implementar un análisis integral que combine técnicas de A/B testing y análisis de datos avanzados. Esto permitirá detectar patrones en el comportamiento del usuario, identificar segmentos de clientes con potencial y establecer estrategias que mejoren tanto la experiencia de navegación como la eficiencia en la generación de ventas.

---

## 2. **Objetivo Principal del Proyecto**

El principal objetivo de este proyecto es desarrollar uno o varios dashboards interactivos que permitan visualizar de forma clara y dinámica los insights derivados del análisis de ventas y comportamiento del usuario. Con este enfoque, los directivos de Amazon podrán:

- **Identificar patrones de comportamiento** en los usuarios, desde la navegación hasta la conversión, facilitando la personalización de las ofertas.
- **Evaluar la efectividad del A/B testing** para determinar qué cambios en la plataforma impactan positivamente en la tasa de conversión y en el valor de las transacciones.
- **Optimizar las estrategias de marketing** y la segmentación de clientes, basándose en variables demográficas, geográficas y comportamentales.
- **Monitorear en tiempo real** indicadores clave de rendimiento (KPIs) como el total de ventas, el ticket promedio, el uso de cupones y la duración de las sesiones.

---

## 3. **Descripción de las Columnas del Conjunto de Datos**

El conjunto de datos generado para este proyecto contiene información detallada sobre las visitas, las transacciones y el comportamiento de los usuarios en la plataforma. A continuación, se presenta una descripción de las columnas más relevantes:

### **Datos de Sesión y Usuario**

- **user_id:** Identificador único para cada sesión o usuario, utilizado para rastrear la actividad de forma individual.
- **group:** Indica la asignación al experimento A/B (grupo "A" o "B"), fundamental para evaluar el impacto de las variantes en la conversión.
- **visit_date:** Fecha en la que se realizó la visita, permitiendo el análisis de tendencias y patrones temporales.
- **session_duration:** Duración de la sesión en minutos, que ayuda a medir el compromiso y la interacción del usuario con la plataforma.

### **Información de la Compra y Comportamiento**

- **conversion:** Variable binaria (0 o 1) que indica si la sesión resultó en una compra.
- **coupon_used:** Indica si se utilizó un cupón durante la transacción
- **payment_method:** Método de pago utilizado en la compra.
- **shipping_method:** Método de envío seleccionado.
- **referral_source:** Fuente de referencia del tráfico

### **Información del Producto y la Transacción**

- **product_category:** Categoría a la que pertenece el producto.
- **product_id:** Código único asignado a cada producto.
- **product_name:** Nombre descriptivo del producto.
- **quantity:** Número de unidades adquiridas en la transacción.
- **price:** Precio unitario del producto.
- **discount:** Porcentaje de descuento aplicado.
- **total_value:** Valor total de la compra.

### **Datos Demográficos y de Navegación**

- **region:** Región geográfica del cliente.
- **customer_age:** Edad del cliente.
- **customer_gender:** Género del cliente.
- **device:** Tipo de dispositivo desde el cual se realizó la visita.
- **browser:** Navegador web utilizado.

---

## 4. **Próximos Pasos**

1. **Recolección y Validación de Datos:**
    
    Consolidar los datos históricos y actuales provenientes de diversas fuentes, asegurando su calidad y consistencia.
    
2. **Análisis Exploratorio de Datos (EDA):**
    
    Realizar un análisis descriptivo y visual para identificar tendencias, outliers y áreas de mejora, así como evaluar la integridad de la información.
    
3. **Transformación y Limpieza de Datos:**
    
    Procesar y normalizar las variables, gestionar los valores nulos y preparar el dataset para el análisis estadístico y la ejecución del A/B testing.
    
4. **Implementación del A/B Testing:**
    
    Diseñar y ejecutar experimentos para comparar las variantes, utilizando técnicas estadísticas para validar las hipótesis de mejora en conversión y ventas.
    
5. **Desarrollo de Dashboards Interactivos:**
    
    Crear dashboards en Power BI que permitan visualizar de manera dinámica los KPIs clave, facilitando el monitoreo y la toma de decisiones estratégicas.
    
6. **Reporte Final y Recomendaciones:**
    
    Elaborar un informe detallado que resuma los hallazgos del análisis y proponga acciones concretas para optimizar la experiencia del usuario y el rendimiento comercial.