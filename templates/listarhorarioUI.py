import streamlit as st
import pandas as pd
from views import View

class ListarHorarioUI:
    def main():
        st.header("Horários Disponíveis")
        ListarHorarioUI.listar()

    def listar():
        horarios = View.horario_listar_disponiveis()
        if len(horarios) == 0:
            st.write("Nenhum horário disponível")
        else: #TODO: não sei se funciona, mas creio que sim
            # dic = []
            # for obj in horarios: dic.append(obj.to_json())
            df = pd.DataFrame(obj.from_dict())
            st.dataframe(df)
