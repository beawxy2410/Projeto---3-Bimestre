import streamlit as st
import pandas as pd
from views import View
import time


class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterServicoUI.listar()
        with tab2:
            ManterServicoUI.inserir()
        with tab3:
            ManterServicoUI.atualizar()
        with tab4:
            ManterServicoUI.excluir()

    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            # for obj in Servicos: st.write(obj)
            dic = []
            for obj in servicos:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe o nome do serviço")
        valor = st.text_input("Informe o valor (R$)")
        duracao = st.text_input("Informe a duração (minutos)")
        if st.button("Inserir"):
            View.servico_inserir(descricao, float(valor), int(duracao))
            st.success("Servico inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Atualização de serviço", servicos)
            descricao = st.text_input(
                "Informe o novo nome do serviço", op.get_descricao()
            )
            valor = st.text_input("Informe o novo valor (R$)", op.get_valor())
            duracao = st.text_input(
                "Informe a nova duração (minutos)", str(op.get_duracao())
            )
            if st.button("Atualizar"):
                View.servico_atualizar(
                    op.get_id(), descricao, float(valor), int(duracao)
                )
                st.success("Serviço atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado.")
        # else:
        #     descricao_para_servico = {
        #         f"ID: {s.get_id()} - Nome: {s.get_nome()}": s for s in servicos
        #     }
        # descricao_escolhida = st.selectbox("Exclusão de serviço", list(descricao_para_servico.keys()))
        servico = st.selectbox("Exclusão de serviço", servicos)
        # servico_escolhido = descricao_para_servico[descricao_escolhida]
        if st.button("Excluir"):
            if servico is None:
                return
            
            try:
                View.servico_excluir(servico.get_id())
                st.success("Serviço excluído com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))
