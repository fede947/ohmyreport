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
            self["Critical"] = "Crítico"
            self["High"] = "Alto"
            self["Medium"] = "Medio"
            self["Low"] = "Bajo"
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
            self["ips"] = "Ips afectados:"

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
            self["introduction-paragraph"] = """ has asked BTR Consulting to perform a security assessment of its infrastructure exposed to the Internet. The purpose of this assessment was to assist the company in evaluating the overall risk of unauthorized access to IT assets and the information contained or managed by them. An attempt was made to identify vulnerabilities that would allow any of the following actions:
            Identity theft to defraud or compromise the Organization or its users,
            Obtaining and access by means of unauthorized users with attributes to create, access or delete information,
            Possibility of gaining access for the administration of the components that make up the Organization's network,
            Access to information available to unauthorized users about the technological infrastructure and its configuration.
            """
            self["objetive"]= "Objetive and scope"
            self["objetive-paragraph"] = """The objective of this project was to identify the degree of exposure to threats and security vulnerabilities of the infrastructure exposed to the Internet of the organization.
In order to meet the objective we carried out an external intrusion attempt on the following ranges of IP addresses provided by the company:
            """
            self["percentage"] = "Detected vulnerabilities percentage"
            self["percentage-paragraph"] = "There have been detected {} vulnerabilities, of which {} have been catalogued as critical, {} as high, {} as medium, {} as low."
            self["cant"] = "Quantity"
            self["Critical"] = "Critical"
            self["High"] = "High"
            self["Medium"] = "Medium"
            self["Low"] = "Low"
            self["observation"] = "Observations"
            self["conclutions"] = "Conclutions"
            self["conclutions-paragraph"] = "Given the defined objectives and scopes, it appears that the external infrastructure under analysis has vulnerabilities that would allow an attacker to enter arbitrary code to the Company's Web services, compromising its operation through DoS and Brute Force attacks."
            self["security-evaluation"] = "Security evaluation of the extern perimiter"
            self["discovery"] = "Discovery"
            self["discovery-paragraph-1"] = "BTR Consulting's team of professionals used publicly available and proprietary tools to analyze the architecture profile of the {} Internet connection, using the following IP addresses provided by the company:"
            self["discovery-paragraph-2"] = """Vulnerabilities and weaknesses were identified on all the IP addresses mentioned. The tasks performed were as follows:
1) Analysis of information available on the Internet, and of public access:
    Searches by words in the most popular Internet portals, such as: Google, Bing and Yahoo.
    Queries to NIC Argentina, a public database, to locate domain names.
2) Identification of weaknesses in the configuration of equipment exposed to the Internet:
    Attempt to collect information from the internal addresses of hosts, accessing the zone information of the Domain Names service (DNS).
    Tracking of communication packets, in order to determine the network topology including routers and firewalls.
    Pinging of hosts with communication packets in order to determine which of them are active.
From the tasks mentioned the following information emerged:
"""
            self["nslookup"] = "Nslookup"
            self["nslookup-paragraph"] = """Nslookup is a public tool used to enumerate "zone information" corresponding to domain name servers. Every computer published on the Internet has a specific network address (IP), just as every house has a street address. Also, each host has a name that corresponds to that network address (IP). Domain name servers are responsible for keeping track of the network addresses associated with a host name. Zone Transfer" is the function that domain name servers have, by which they share zone information among themselves.

Additionally, the Dig and Fierce tools were used, which have functionalities analogous to those of Nslookup, allowing the zone transfer to be tested. The result of these programs is shown below:
"""
            self["whois"] = "Whois"
            self["whois-paragraph"] = """"Whois" is a program used to extract public administrative information registered on the Internet. Anyone can extract IP addresses, phone numbers and contact names from the registrar's database.

Published information is required to own an IP range on the Internet. However, in this way an attacker begins with the recognition of the team in an effort to focus the attack.

Typical results show information such as network address ranges, physical addresses, contact names and phone numbers.
"""
            self["traceroute"] = "Traceroute"
            self["traceroute-paragraph"] = """Traceroute, is used to associate the network path taken from one main computer to another. The purpose is to track these communication paths in order to obtain additional information about the Company's network configuration. In this way, Firewalls and Routers can be identified and become targets for information gathering. The information obtained is also available to anyone connected to the Internet, but this does not necessarily imply a high risk.

Trace uses ICMP packets which in many cases are filtered so it is not always possible to obtain such information. In order to avoid this situation, different packet modification techniques are used in order to avoid the filtering normally carried out by firewalls and routers and to obtain information about the hosts as shown below:
"""
            self["port-scan"] = "Port scanning results"
            self["port-scan-paragraph"] = "The following table shows the results of the port scanning and banner acquisition performed"
            self["vulnerabilities-identification"] = "Vulnerabilities identification"
            self["vulnerabilities-identification-paragraph"] = """The addresses identified during Phase 1 were scanned with our own tools and others for public use, in order to determine the operating systems and services enabled in the Company's network. A Banner acquisition was then performed to determine the systems and software versions running on the hosts.

The identification of the operating system is done through TCP/IP "OS fingerprinting" techniques. By abusing the different ways in which software companies implement the TCP/IP stack, the scanning tools perform a comparison of these stacks against a database, thus determining the type and version of the operating systems.

The Banner acquisition technique allows additional information to be collected in order to more accurately identify the operating system running on each host. Once this information has been collected, it is possible to relate it to a vulnerability specific to each operating system.

Given that communication ports represent a potential access route, BTR Consulting professionals performed a port scan using intrusion detection system (IDS) evasion techniques to identify those that are open, in order to find potential vulnerabilities associated with them.

Using the information acquired during the port scanning and the acquisition of banners, the professionals of BTR Consulting carried out a search for vulnerabilities using their own tools, others available on the Internet and manual techniques in order to be able to detect the existing weaknesses in the open ports.
"""
            self["explotation"] = "Explotation"
            self["explotation-paragraph"] = "BTR Consulting's professionals used the information gathered in the vulnerability identification phase to apply intrusive techniques in order to obtain unauthorized access to the Company's hosts. Although no vulnerabilities were detected that would allow access to the devices of the redexposed {}, some vulnerabilities and weaknesses of configuration were detected, which although they did not conclude in the commitment of the integrity of the external network, require modifications with the objective of reinforcing the security of the IT environment."
            self["recomendation"] = "Vulnerabilities and associated recommendations"
            self["recomendation-paragraph"] = "The following recommendations should be implemented with the objective of improving the safety of the Company's technology environment. While the recommendations herein have been tested by BTR Consulting, they should be tested in non-productive schedules and {} test environments. It is also advisable to have full backups before implementing the recommendations described here, ensuring proper functionality and continuity of processing."
            self["ips"] = "Affected ips:"
