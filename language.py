class Language(dict):

    def __init__(self,language):
        if(language == 'es'):
            self["identification-title"] = 'Identificacion'
            self["vulnerability-title"] = 'Deteccion de vulnerabilidad'
            self["exploitation-title"] = 'Explotacion'
            self["detailed-title"] = 'Detalles y recomendaciones'
            self["vulnerability-title-table"] = 'Vulnerabilidad:'
            self["risk-title-table"] = 'Riesgo:'
            self["description-title-table"] = 'Descripcion:'
            self["solution-title-table"] = 'Recomendacion:'
            self["impact-title-table"] = 'Impacto de Negocio:'
            self["management-title-table"] = 'Respuesta gerencial:'
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


        if(language == 'en'):
            self["identification-title"] = 'Identification'
            self["vulnerability-title"] = 'Vulnerability detection'
            self["exploitation-title"] = 'Exploitation'
            self["detailed-title"] = 'Detailed findings and recommendations'
            self["vulnerability-title-table"] = 'Vulnerability:'
            self["risk-title-table"] = 'Risk Factor:'
            self["description-title-table"] = 'Description:'
            self["solution-title-table"] = 'recommendations:'
            self["impact-title-table"] = 'Impact of business:'
            self["management-title-table"] = 'Gerential management:'
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
