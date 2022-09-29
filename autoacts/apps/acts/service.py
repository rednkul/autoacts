def describe_project(project):
    print(f'{project.id}.{project.name}')
    print(f'Кол-во актов в проекте:{project.acts.count()}')
    for act in project.acts.all():
        print(act, act.number)
        print(f'Работы: {act.works}')
        print(f'{act.date_start} - {act.date_end}')
        print(f'Материалов в акте:{act.materials.count()}')
        print('Материалы:')
        for material in act.materials.all():
            print(f'{material.name} -  {material.filename}')