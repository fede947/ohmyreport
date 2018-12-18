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
