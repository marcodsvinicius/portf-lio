files = ['Case-Design-System.html','Case-Hub-de-Obras.html','Case-Rebalanceamento-Carteira.html','Case-Tour-Guiado.html']
for f in files:
    c = open(f, encoding='utf-8').read()
    has_fixed = 'fixed bottom-6 right-6 md:right-12' in c
    has_icon  = 'arrow-up' in c
    in_header = 'flex items-center gap-2' in c
    print(f'{f}:')
    print(f'  fixed bottom-right: {has_fixed}')
    print(f'  arrow-up icon:      {has_icon}')
    print(f'  btt still in header:{in_header}')
