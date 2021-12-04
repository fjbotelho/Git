# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

# Read data from file 'filename.csv' 
# 
# 'data'',''data_dados'',''confirmados','confirmados_arsnorte','confirmados_arscentro','confirmados_arslvt','confirmados_arsalentejo','confirmados_arsalgarve','confirmados_acores','confirmados_madeira','confirmados_estrangeiro','confirmados_novos','recuperados','obitos','internados','internados_uci','lab','suspeitos','vigilancia','n_confirmados','cadeias_transmissao','transmissao_importada','confirmados_0_9_f','confirmados_0_9_m','confirmados_10_19_f','confirmados_10_19_m','confirmados_20_29_f','confirmados_20_29_m','confirmados_30_39_f','confirmados_30_39_m','confirmados_40_49_f','confirmados_40_49_m','confirmados_50_59_f','confirmados_50_59_m','confirmados_60_69_f','confirmados_60_69_m','confirmados_70_79_f','confirmados_70_79_m','confirmados_80_plus_f','confirmados_80_plus_m','sintomas_tosse','sintomas_febre','sintomas_dificuldade_respiratoria','sintomas_cefaleia','sintomas_dores_musculares','sintomas_fraqueza_generalizada','confirmados_f','confirmados_m','obitos_arsnorte','obitos_arscentro','obitos_arslvt','obitos_arsalentejo','obitos_arsalgarve','obitos_acores','obitos_madeira','obitos_estrangeiro','recuperados_arsnorte','recuperados_arscentro','recuperados_arslvt','recuperados_arsalentejo','recuperados_arsalgarve','recuperados_acores','recuperados_madeira','recuperados_estrangeiro','obitos_0_9_f','obitos_0_9_m','obitos_10_19_f','obitos_10_19_m','obitos_20_29_f','obitos_20_29_m','obitos_30_39_f','obitos_30_39_m','obitos_40_49_f','obitos_40_49_m','obitos_50_59_f','obitos_50_59_m','obitos_60_69_f','obitos_60_69_m','obitos_70_79_f','obitos_70_79_m','obitos_80_plus_f','obitos_80_plus_m','obitos_f','obitos_m' 
df = pd.read_csv('data.csv', usecols=['data', 'confirmados'], index_col ='data') 

# add new columns
#df['diferenca']=0
#df['percentagem']=0

row_num = len(df.index) 

print ('-> ', row_num)
print (df.tail())

#print (df.dtypes)

df['diferenca'] = df['confirmados'] - df['confirmados'].shift()
df['percentagem'] = (df['confirmados'] / df['confirmados'].shift()) - 1
df['estimado'] = 1.0
df['estimado'] = df['estimado'] + df['estimado'].shift() * 1.3

print (df.tail())

