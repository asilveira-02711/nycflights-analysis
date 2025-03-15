def create_db(engine):

    meta = MetaData()
    flights = Table('flights', meta,
        Column('data_hora', String, nullable=False),
        Column('atraso_chegada', Float),
        Column('companhia', String),
        Column('id_voo', String),
        Column('tempo_voo', Float),
        Column('distancia', Float),
        Column('origem', String(60)),
        Column('destino', String(60),
        Column('tempo_minutos', Float),
        Column('periodo', String(20)))
        # criar as novas colunas aqui
    )

    flights.create(engine)
