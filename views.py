from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
        for c in View.cliente_listar():
            if c.get_email() == email:
                raise ValueError(f"O e-mail '{email}' já está cadastrado.")
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_id() != id:
                raise ValueError(f"O e-mail '{email}' já está cadastrado.")
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        for h in View.horario_listar():
            if h.get_id_cliente() == id:
                raise ValueError(f"O cliente com ID '{id}' possui horários agendados e não pode ser excluído.")
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)   

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome() }
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        if confirmado:
            for c in View.cliente_listar():
                if c.get_id() == id_cliente:
                    break
            else:
                raise ValueError(f"O cliente com ID '{id_cliente}' não existe.")
            
            for s in View.servico_listar():
                if s.get_id() == id_servico:
                    break
            else:
                raise ValueError(f"O serviço com ID '{id_servico}' não existe.")

        h = Horario(0, data, confirmado, id_cliente, id_servico)
        Horarios.inserir(h)

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.get_data() >= datetime.now() and h.get_id_cliente() == None: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        for c in View.cliente_listar():
            if c.get_id() == id_cliente:
                break
        else:
            raise ValueError(f"O cliente com ID '{id_cliente}' não existe.")
        
        for s in View.servico_listar():
            if s.get_id() == id_servico:
                break
        else:
            raise ValueError(f"O serviço com ID '{id_servico}' não existe.")

        c = Horario(id, data, confirmado, id_cliente, id_servico)
        Horarios.atualizar(c)

    def horario_excluir(id):
        for h in View.horario_listar():
            if h.get_id() == id and h.get_id_cliente() is not None:
                raise ValueError(f"O horário com ID '{id}' está agendado para um cliente e não pode ser excluído.")
        c = Horario(id, None)
        Horarios.excluir(c)    

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        try:
            di = datetime.strptime(f"{data} {hora_inicio}", "%d/%m/%Y %H:%M")
            df = datetime.strptime(f"{data} {hora_fim}", "%d/%m/%Y %H:%M")
            if di >= df:
                raise ValueError("A hora inicial deve ser anterior à hora final.")
            if intervalo <= 0:
                raise ValueError("O intervalo deve ser maior que zero.")
            if df - di < timedelta(minutes=intervalo):
                raise ValueError("O intervalo é maior que o período especificado.")
        except ValueError as e:
            raise ValueError(f"Erro nos parâmetros fornecidos: {e}")
        x = di
        while x <= df:
            View.horario_inserir(x, False, None, None) 
            x += timedelta(minutes=intervalo)  


    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        for h in View.horario_listar():
            if h.get_id_servico() == id:
                raise ValueError(f"O serviço com ID '{id}' aparece na agenda e não pode ser excluído.")
        c = Servico(id, "", 0, 0)
        Servicos.excluir(c)  
