import streamlit as st
from services.crud import tasks_db, create_task, get_tasks, update_task, delete_task
from models.task import Task

def main():
    st.title("Lista de Tarefas")

    # Formulário para adicionar uma nova tarefa
    with st.form(key='task_form'):
        title = st.text_input("Título da Tarefa")
        description = st.text_area("Descrição da Tarefa")
        submitted = st.form_submit_button("Adicionar Tarefa")
        if submitted:
            create_task(tasks_db, title, description)
            st.success("Tarefa adicionada com sucesso!")

    # Exibir lista de tarefas
    tasks = get_tasks()
    for task in tasks:
        task_id = task['id']
        st.subheader(task['title'])
        st.write(task['description'])
        st.checkbox("Concluída", value=task['completed'], key=task_id)

        # Botões para editar e remover tarefas
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Editar", key=f'edit_{task_id}'):
                new_title = st.text_input("Novo Título", value=task.title)
                new_description = st.text_area("Nova Descrição", value=task.description)
                if st.button("Salvar", key=f'save_{task_id}'):
                    update_task(tasks_db, task_id, new_title, new_description)
                    st.success("Tarefa atualizada com sucesso!")

        with col2:
            if st.button("Remover", key=f'remove_{task_id}'):
                delete_task(tasks_db, task_id)
                st.success("Tarefa removida com sucesso!")

if __name__ == "__main__":
    main()