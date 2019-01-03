class Language(dict):

    def __init__(self,language):
        if(language == 'es'):
            self["identification-title"] = 'Identificación'
            self["vulnerability-title"] = 'Deteccion de vulnerabilidad'
            self["exploitation-title"] = 'Explotación'
            self["detailed-title"] = 'Detalles y recomendaciones'
            self["vulnerability-title-table"] = 'Vulnerabilidad:'
            self["risk-title-table"] = 'Riesgo:'
            self["description-title-table"] = 'Descripción:'
            self["solution-title-table"] = 'Recomendación:'
            self["impact-title-table"] = 'Impacto de Negocio:'
            self["management-title-table"] = 'Respuesta gerencial:'
            self["category-title-table"] = "Categoria:"
            self["CVSS-title-table"] = "CVSS score:"
            self["CVE-title-table"] = "CVE:"
            self["effort-title-table"] = "Esfuerzo para repararla:"
            self["exploit-subtitle"] = 'Vulnerabilidad no explotada'
            self["content"] = "Contenido"
            self["executive-summary"] = "Reporte ejecutivo"
            self["introduction"] = "Introducción"
            self["introduction-paragraph"] = """ ha solicitado a BTR Consulting efectuar una evaluación de seguridad a su infraestructura expuesta a internet. El propósito de esta evaluación consistió en brindar asistencia a la compañía en la evaluación del riesgo general de los accesos no autorizados a los activos de Tecnología Informática y la información contenida o gestionada por los mismos. Se trataron de identificar vulnerabilidades que permitieran, alguna de las siguientes acciones:
            Robo de identidad para defraudar o comprometer a la Organización o a sus usuarios,
            Obtención y accesos por medio de usuarios no autorizados con atributos para crear, acceder o borrar información,
            Posibilidad de lograr el acceso para la administración de los componentes que conforman la red de la Organización,
            Acceso a información disponible a usuarios no autorizados sobre la infraestructura tecnológica y su configuración.
            """
            self["objetive"]= "Objetivo y alcance"
            self["objetive-paragraph"] = """El objetivo del presente proyecto consistió en la identificación del grado de exposición a las amenazas y vulnerabilidades de seguridad de la infraestructura expuesta a internet de la organización.
Para cumplir con el objetivo planteado llevamos a cabo un Intento de intrusión externo sobre los siguientes rangos de direcciones IP provistas por la compañía:
            """
            self["percentage"] = "Porcentaje de vulnerabilidades detectadas"
            self["percentage-paragraph"] = "Se han detectado {} vulnerabilidades, de las cuales {} han sido catalogadas como criticas, {} como altas, {} como medias, {} como bajas"
            self["cant"] = "Cantidad"
            self["critical-risk"] = "Critico"
            self["high-risk"] = "Alta"
            self["medium-risk"] = "Media"
            self["low-risk"] = "Baja"
            self["observation"] = "Observaciones"
            self["conclutions"] = "Conclusiones"
            self["conclutions-paragraph"] = "Dado los objetivos y alcances definidos, surge que la infraestructura externa bajo análisis posee vulnerabilidades que permitirían a un atacante ingresar código arbitrario a servicios Web de la Compañía, comprometiendo la operatividad del mismo mediante ataques DoS y Fuerza Bruta."
            self["security-evaluation"] = "Evaluación de seguridad del perimitro externo"
            self["discovery"] = "Discovery"
            self["discovery-paragraph-1"] = "El equipo de profesionales de BTR Consulting utilizó herramientas públicas disponibles y propias para analizar el perfil de la arquitectura de {} conectada a Internet, utilizando las siguientes direcciones IP provistas por la compañía:"
            self["discovery-paragraph-2"] = """Sobre todas las direcciones IP mencionadas se realizó una identificación de vulnerabilidades y debilidades. Las tareas realizadas fueron las siguientes:
1) Análisis de información disponible en Internet, y de acceso público:
    Búsquedas por palabras en los portales más populares de Internet, tales como: Google, Bing y Yahoo.
    Consultas a NIC Argentina, una base de datos pública, para localizar nombres de dominio.
2) Identificación de debilidades en la configuración de los equipos expuestos a Internet:
    Intento de recopilar información de las direcciones internas de los hosts, accediendo a la información de zona del servicio de Nombres de Dominio (DNS).
    Rastreo de paquetes de comunicación, con el fin de determinar la topología de red incluyendo routers y firewalls.
    Pinging de hosts con paquetes de comunicación con el objetivo de determinar cuáles de ellos se encuentran activos.
De las tareas mencionadas surgió la siguiente información:
"""
            self["nslookup"] = "Nslookup"
            self["nslookup-paragraph"] = """Nslookup es una herramienta pública utilizada para enumerar “información de zona” correspondiente a servidores de nombres de dominio. Todo equipo publicado en Internet posee una dirección de red específica (IP), así como cada casa posee una dirección de calle. Así también, cada host posee un nombre que se corresponde con esa dirección de red (IP). Los servidores de nombre de dominio son los responsables de mantener registro de las direcciones de red asociadas a un nombre de host. Se denomina “Transferencia de Zona” a la función que poseen los servidores de nombres de dominio, por la cual comparten información de zona entre ellos.

Adicionalmente se utilizaron las herramientas Dig y Fierce las cuales poseen funcionalidades análogas a las de Nslookup permitiendo probar la transferencia de zona. A continuación se expone el resultado de dichos programas:
"""
            self["whois"] = "Whois"
            self["whois-paragraph"] = """“Whois”, es un programa utilizado para extraer información administrativa pública registrada en Internet. Cualquier persona puede extraer direcciones IP, números de teléfono y nombres de contactos desde la base de datos del registrador.

La información publicada es requerida para ser dueño de un rango IP en Internet. Sin embargo, de esta manera un atacante comienza con el reconocimiento del equipo en un esfuerzo de enfocar el ataque.

Los resultados típicos muestran información tal como rangos de direcciones de red, direcciones físicas, nombres de contacto y números de teléfono.
"""
            self["traceroute"] = "Traceroute"
            self["traceroute-paragraph"] = """Traceroute, se utiliza para asociar el camino de la red tomado a partir de una computadora principal a otra. El propósito es rastrear estos caminos de comunicaciones para así obtener información adicional acerca de la configuración de red de la Compañía. De esta manera, se pueden identificar Firewalls y Routers que pueden convertirse en blancos para la reunión de información. La información obtenida también se encuentra disponible para cualquier persona conectada a Internet, pero esto no implica, necesariamente, un alto riesgo.

Trace utiliza paquetes ICMP los cuales en muchos casos se encuentran filtrados por lo que no siempre es posible obtener dicha información. Para evitar dicha situación se utilizan diferentes técnicas de modificación de paquetes para así evadir el filtrado que normalmente realizan firewalls y routers y obtener la información sobre los hosts como se ve a continuación:
"""
            self["port-scan"] = "Resultados del escaneo de puertos"
            self["port-scan-paragraph"] = "La siguiente tabla muestra los resultados del escaneo de puertos y adquisición de banners realizado"
            self["vulnerabilities-identification"] = "Identificación de vulnerabilidades"
            self["vulnerabilities-identification-paragraph"] = """Se realizó un escaneo a las direcciones identificadas durante la Fase 1 con herramientas propias y con otras de uso público, con el propósito de determinar los sistemas operativos y servicios habilitados en la red de la Compañía. Luego se realizó un “Banner acquisition” para determinar los sistemas y versiones del software que se ejecutan en los hosts.

La identificación del sistema operativo es realizada por medio de técnicas de TCP/IP “OS fingerprinting”. Abusando de las diferentes formas en que las empresas de software implementan el “stack” de TCP/IP, las herramientas de escaneo realizan una comparación de estos stacks contra una base de datos, determinando así el tipo y versión de los sistemas operativos.

La técnica de “Banner acquisition” permite recopilar información adicional, con el fin de identificar de una manera más certera el sistema operativo que se ejecuta en cada host. Una vez recopilada dicha información, es posible relacionarla con una vulnerabilidad propia de cada sistema operativo. 

Dado que los puertos de comunicación representan una potencial vía de acceso, los profesionales de BTR Consulting realizaron un escaneo de puertos utilizando técnicas de evasión de sistemas de detección de intrusos (IDS) para identificar aquellos que se encuentran abiertos, con el fin de hallar potenciales vulnerabilidades asociadas a los mismos.

Utilizando la información adquirida durante el escaneo de puertos y la obtención de banners, los profesionales de BTR Consulting realizaron una búsqueda de vulnerabilidades utilizando herramientas propias, otras disponibles en Internet y técnicas manuales a fin de poder detectar las debilidades existentes en los puertos abiertos.
"""
            self["explotation"] = "Explotación"
            self["explotation-paragraph"] = "Los profesionales de BTR Consulting utilizaron la información recopilada en la fase de identificación de vulnerabilidades, para aplicar técnicas intrusivas con el objetivo de obtener acceso no autorizado a los hosts de la Compañía. Si bien no se detectaron vulnerabilidades que permitirían el acceso a los dispositivos de la redexpuesta de [empresa], se detectaron algunas vulnerabilidades y debilidades de configuración, que si bien no concluyeron en el compromiso de la integridad de la red externa, requieren de modificaciones con el objetivo de reforzar la seguridad del entorno de TI."
            self["recomendation"] = "Vulnerabilidades y recomendaciones asociadas"
            self["recomendation-paragraph"] = "Las siguientes son recomendaciones deberían ser aplicadas con el objetivo de mejorar la seguridad del ambiente de tecnología de la Compañía. Si bien las recomendaciones aquí expuestas han sido probadas por BTR Consulting, deberían ser probadas en horarios no productivos y entornos de prueba de [empresa]. Asimismo resulta recomendable disponer de full backups antes de implementar las recomendaciones aquí descritas, asegurando la correcta funcionalidad y continuidad del procesamiento."

        if(language == 'en'):
            self["identification-title"] = 'Identification'
            self["vulnerability-title"] = 'Vulnerability detection'
            self["exploitation-title"] = 'Exploitation'
            self["detailed-title"] = 'Detailed findings and recommendations'
            self["vulnerability-title-table"] = 'Vulnerability:'
            self["risk-title-table"] = 'Risk Factor:'
            self["description-title-table"] = 'Description:'
            self["solution-title-table"] = 'Recommendations:'
            self["impact-title-table"] = 'Business impact:'
            self["management-title-table"] = 'Gerential management:'
            self["category-title-table"] = "Category:"
            self["CVSS-title-table"] = "CVSS score:"
            self["CVE-title-table"] = "CVE:"
            self["effort-title-table"] = "Effort to fix:"
            self["exploit-subtitle"] = 'Vulnerability no exploited'
            self["content"] = "Content"
            self["executive-summary"] = "Executive summary"
            self["introduction"] = "Introduction"
            self["introduction-paragraph"] = """ ha solicitado a BTR Consulting efectuar una evaluación de seguridad a su infraestructura expuesta a internet. El propósito de esta evaluación consistió en brindar asistencia a la compañía en la evaluación del riesgo general de los accesos no autorizados a los activos de Tecnología Informática y la información contenida o gestionada por los mismos. Se trataron de identificar vulnerabilidades que permitieran, alguna de las siguientes acciones:
            Robo de identidad para defraudar o comprometer a la Organización o a sus usuarios,
            Obtención y accesos por medio de usuarios no autorizados con atributos para crear, acceder o borrar información,
            Posibilidad de lograr el acceso para la administración de los componentes que conforman la red de la Organización,
            Acceso a información disponible a usuarios no autorizados sobre la infraestructura tecnológica y su configuración.
            """
            self["objetive"]= "Objetive and scope"
            self["objetive-paragraph"] = """El objetivo del presente proyecto consistió en la identificación del grado de exposición a las amenazas y vulnerabilidades de seguridad de la infraestructura expuesta a internet de la organización.
Para cumplir con el objetivo planteado llevamos a cabo un Intento de intrusión externo sobre los siguientes rangos de direcciones IP provistas por la compañía:
            """
            self["percentage"] = "Detected vulnerabilities percentage"
            self["percentage-paragraph"] = "Se han detectado {} vulnerabilidades, de las cuales {} han sido catalogadas como criticas, {} como altas, {} como medias, {} como bajas"
            self["cant"] = "Quantity"
            self["critical-risk"] = "Critical"
            self["high-risk"] = "High"
            self["medium-risk"] = "Medium"
            self["low-risk"] = "Low"
            self["observation"] = "Observations"
            self["conclutions"] = "Conclutions"
            self["conclutions-paragraph"] = "Dado los objetivos y alcances definidos, surge que la infraestructura externa bajo análisis posee vulnerabilidades que permitirían a un atacante ingresar código arbitrario a servicios Web de la Compañía, comprometiendo la operatividad del mismo mediante ataques DoS y Fuerza Bruta."
            self["security-evaluation"] = "Security evaluation of the extern perimiter"
            self["discovery"] = "Discovery"
            self["discovery-paragraph-1"] = "El equipo de profesionales de BTR Consulting utilizó herramientas públicas disponibles y propias para analizar el perfil de la arquitectura de {} conectada a Internet, utilizando las siguientes direcciones IP provistas por la compañía:"
            self["discovery-paragraph-2"] = """Sobre todas las direcciones IP mencionadas se realizó una identificación de vulnerabilidades y debilidades. Las tareas realizadas fueron las siguientes:
1) Análisis de información disponible en Internet, y de acceso público:
    Búsquedas por palabras en los portales más populares de Internet, tales como: Google, Bing y Yahoo.
    Consultas a NIC Argentina, una base de datos pública, para localizar nombres de dominio.
2) Identificación de debilidades en la configuración de los equipos expuestos a Internet:
    Intento de recopilar información de las direcciones internas de los hosts, accediendo a la información de zona del servicio de Nombres de Dominio (DNS).
    Rastreo de paquetes de comunicación, con el fin de determinar la topología de red incluyendo routers y firewalls.
    Pinging de hosts con paquetes de comunicación con el objetivo de determinar cuáles de ellos se encuentran activos.
De las tareas mencionadas surgió la siguiente información:
"""
            self["nslookup"] = "Nslookup"
            self["nslookup-paragraph"] = """Nslookup es una herramienta pública utilizada para enumerar “información de zona” correspondiente a servidores de nombres de dominio. Todo equipo publicado en Internet posee una dirección de red específica (IP), así como cada casa posee una dirección de calle. Así también, cada host posee un nombre que se corresponde con esa dirección de red (IP). Los servidores de nombre de dominio son los responsables de mantener registro de las direcciones de red asociadas a un nombre de host. Se denomina “Transferencia de Zona” a la función que poseen los servidores de nombres de dominio, por la cual comparten información de zona entre ellos.

Adicionalmente se utilizaron las herramientas Dig y Fierce las cuales poseen funcionalidades análogas a las de Nslookup permitiendo probar la transferencia de zona. A continuación se expone el resultado de dichos programas:
"""
            self["whois"] = "Whois"
            self["whois-paragraph"] = """“Whois”, es un programa utilizado para extraer información administrativa pública registrada en Internet. Cualquier persona puede extraer direcciones IP, números de teléfono y nombres de contactos desde la base de datos del registrador.

La información publicada es requerida para ser dueño de un rango IP en Internet. Sin embargo, de esta manera un atacante comienza con el reconocimiento del equipo en un esfuerzo de enfocar el ataque.

Los resultados típicos muestran información tal como rangos de direcciones de red, direcciones físicas, nombres de contacto y números de teléfono.
"""
            self["traceroute"] = "Traceroute"
            self["traceroute-paragraph"] = """Traceroute, se utiliza para asociar el camino de la red tomado a partir de una computadora principal a otra. El propósito es rastrear estos caminos de comunicaciones para así obtener información adicional acerca de la configuración de red de la Compañía. De esta manera, se pueden identificar Firewalls y Routers que pueden convertirse en blancos para la reunión de información. La información obtenida también se encuentra disponible para cualquier persona conectada a Internet, pero esto no implica, necesariamente, un alto riesgo.

Trace utiliza paquetes ICMP los cuales en muchos casos se encuentran filtrados por lo que no siempre es posible obtener dicha información. Para evitar dicha situación se utilizan diferentes técnicas de modificación de paquetes para así evadir el filtrado que normalmente realizan firewalls y routers y obtener la información sobre los hosts como se ve a continuación:
"""
            self["port-scan"] = "Port scanning results"
            self["port-scan-paragraph"] = "La siguiente tabla muestra los resultados del escaneo de puertos y adquisición de banners realizado"
            self["vulnerabilities-identification"] = "Vulnerabilities identification"
            self["vulnerabilities-identification-paragraph"] = """Se realizó un escaneo a las direcciones identificadas durante la Fase 1 con herramientas propias y con otras de uso público, con el propósito de determinar los sistemas operativos y servicios habilitados en la red de la Compañía. Luego se realizó un “Banner acquisition” para determinar los sistemas y versiones del software que se ejecutan en los hosts.

La identificación del sistema operativo es realizada por medio de técnicas de TCP/IP “OS fingerprinting”. Abusando de las diferentes formas en que las empresas de software implementan el “stack” de TCP/IP, las herramientas de escaneo realizan una comparación de estos stacks contra una base de datos, determinando así el tipo y versión de los sistemas operativos.

La técnica de “Banner acquisition” permite recopilar información adicional, con el fin de identificar de una manera más certera el sistema operativo que se ejecuta en cada host. Una vez recopilada dicha información, es posible relacionarla con una vulnerabilidad propia de cada sistema operativo.

Dado que los puertos de comunicación representan una potencial vía de acceso, los profesionales de BTR Consulting realizaron un escaneo de puertos utilizando técnicas de evasión de sistemas de detección de intrusos (IDS) para identificar aquellos que se encuentran abiertos, con el fin de hallar potenciales vulnerabilidades asociadas a los mismos.

Utilizando la información adquirida durante el escaneo de puertos y la obtención de banners, los profesionales de BTR Consulting realizaron una búsqueda de vulnerabilidades utilizando herramientas propias, otras disponibles en Internet y técnicas manuales a fin de poder detectar las debilidades existentes en los puertos abiertos.
"""
            self["explotation"] = "Explotation"
            self["explotation-paragraph"] = "Los profesionales de BTR Consulting utilizaron la información recopilada en la fase de identificación de vulnerabilidades, para aplicar técnicas intrusivas con el objetivo de obtener acceso no autorizado a los hosts de la Compañía. Si bien no se detectaron vulnerabilidades que permitirían el acceso a los dispositivos de la redexpuesta de {}, se detectaron algunas vulnerabilidades y debilidades de configuración, que si bien no concluyeron en el compromiso de la integridad de la red externa, requieren de modificaciones con el objetivo de reforzar la seguridad del entorno de TI."
            self["recomendation"] = "Vulnerabilities and associated recommendations"
            self["recomendation-paragraph"] = "Las siguientes son recomendaciones deberían ser aplicadas con el objetivo de mejorar la seguridad del ambiente de tecnología de la Compañía. Si bien las recomendaciones aquí expuestas han sido probadas por BTR Consulting, deberían ser probadas en horarios no productivos y entornos de prueba de {}. Asimismo resulta recomendable disponer de full backups antes de implementar las recomendaciones aquí descritas, asegurando la correcta funcionalidad y continuidad del procesamiento."
    