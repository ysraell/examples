import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import pandas as pd
import random
import matplotlib.pyplot as plt

@st.cache
def load_data():
    return pd.read_csv('Adult_Census_Income.csv')

df = load_data()

target = 'income'
black_cols = ['fnlwgt','education.num','income']
features = df.columns.tolist()
for col in black_cols:
    features.pop(features.index(col))

black_cols.extend(['capital.gain','capital.loss'])
features_num = ['age','hours.per.week']

features = df.columns.tolist()
for col in black_cols:
    features.pop(features.index(col))

features_cat = features
for col in features_num:
    features_cat.pop(features_cat.index(col))

features = []
features.extend(features_cat)
features.extend(features_num)
features_label = {}
for feat in features:
    features_label[feat] = " ".join([x.capitalize() for x in feat.split('.')])

black_vals = ['?']
features_cat_dict = {}
for col in features_cat:
    tmp = df[col].unique().tolist()
    for val in black_vals:
        if val in tmp:
            tmp.pop(tmp.index(val))
    features_cat_dict[col] = tmp

features_num_dict = {}
for col in features_num:
    tmp = df[col].unique().tolist()
    for val in black_vals:
        if val in tmp:
            tmp.pop(tmp.index(val))
    features_num_dict[col] = sorted(tmp)

def plot_pie(s):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = ['Rich', 'Not Rich']
    colors = ['blue', 'coral']
    sizes = [s, 100-s]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    plt.legend()
    st.pyplot()

def show_results_random(some_cats):
    #some_cats = ['education','age','marital.status','sex']
    while True:
        df_tmp = df[some_cats].sample()
        if all([not val in df_tmp.values.tolist()[0] for val in black_vals]):
            break
    cond_total = (df[some_cats[0]] != black_vals[0])
    if len(black_vals)>1:
        for val in black_vals:
            cond_total = (cond_total & (df[some_cats[0]] != val))
    cond = (df[some_cats[0]] == df_tmp[some_cats[0]].values.tolist()[0])
    if len(some_cats)>1:
        for col in some_cats[1:]:
            cond = (cond & (df[col] == df_tmp[col].values.tolist()[0]))
            cond_total = (cond_total & (df[col] != black_vals[0]))
            if len(black_vals)>1:
                for val in black_vals:
                    cond_total = (cond_total & (df[col] != val))
    df_pop = df.loc[cond]
    target_val = '>50K'
    tg_vals = ((df_pop[target] == '>50K')*1).values.tolist()
    N = cond_total.sum()
    n = len(tg_vals)
    p = 100*sum(tg_vals)/n
    s = 100*n/N
    st.write(df_tmp)
    plot_pie(s)
    st.write("P(Rich) = {:.2f}%, with {:,}/{:,} ({:.4f}%) of the entire dataset.".format(p,n,N,s))
    return df_pop

def show_results(values_feat_choosen):
    some_cats = list(values_feat_choosen.keys())
    cond_total = (df[some_cats[0]] != black_vals[0])
    if len(black_vals)>1:
        for val in black_vals:
            cond_total = (cond_total & (df[some_cats[0]] != val))
    cond = (df[some_cats[0]] == values_feat_choosen[some_cats[0]])
    if len(some_cats)>1:
        for col in some_cats[1:]:
            cond = (cond & (df[col] == values_feat_choosen[col]))
            cond_total = (cond_total & (df[col] != black_vals[0]))
            if len(black_vals)>1:
                for val in black_vals:
                    cond_total = (cond_total & (df[col] != val))
    df_pop = df.loc[cond]
    target_val = '>50K'
    tg_vals = ((df_pop[target] == '>50K')*1).values.tolist()
    N = cond_total.sum()
    n = len(tg_vals)
    if n>0:
        p = 100*sum(tg_vals)/n
        s = 100*n/N
        plot_pie(s)
        st.write("P(Rich) = {:.2f}%, with {:,}/{:,} ({:.4f}%) of the entire dataset.".format(p,n,N,s))
    else:
        st.write("Have not enough data for this values, try another values")
    return df_pop


st.title('What is your chance to be rich?')

Fst_subtitle = st.empty()
Snd_subtitle = st.empty()
Fst_subtitle.subheader('<-- Try a random pick.')
st.sidebar.subheader('Settings')
s_pop = st.sidebar.checkbox('Show population?')
button = st.sidebar.button('Random one?')
if button:
    tmp = list(features_label.keys())
    random.shuffle(tmp)
    some_cats = tmp[:random.randint(1,len(tmp))]
    df_pop = show_results_random(some_cats)
    Fst_subtitle.subheader('A random pick:')
    if s_pop:
        st.write(df_pop)
else:
    st.write()

#st.sidebar.subheader('')
feat_label_choosen = st.sidebar.multiselect('What characteristics?',list(features_label.values()))

N_choosen = len(feat_label_choosen)
if N_choosen>0:
    feat_choosen = []
    for feat, label in features_label.items():
        if label in feat_label_choosen:
            feat_choosen.append(feat)
    if N_choosen<2:
        tmp = '{}:'.format(feat_label_choosen[0])
    elif N_choosen<3:
        tmp = '{} and {}:'.format(feat_label_choosen[0],feat_label_choosen[1])
    elif N_choosen>=3:
        tmp = '{} and {}:'.format(", ".join(feat_label_choosen[:-1]),feat_label_choosen[-1])
    Fst_subtitle.subheader('Choosing {}'.format(tmp))

    if st.sidebar.button('Random person!'):
        Fst_subtitle.subheader('A random pick for {}'.format(tmp))
        df_pop = show_results_random(feat_choosen)
        if s_pop:
            st.write(df_pop)

    if st.sidebar.checkbox('Set more details.'):
        values_feat_choosen = {}
        for feat in feat_choosen:
            text_tmp = 'Value for {}:'.format(features_label[feat])
            if feat in features_cat_dict.keys():
                values_feat_choosen[feat] = st.sidebar.selectbox(text_tmp,features_cat_dict[feat])
            if feat in features_num_dict.keys():
                values_feat_choosen[feat] = st.sidebar.slider(text_tmp,features_num_dict[feat][0],features_num_dict[feat][-1],33)
        if len(values_feat_choosen)>0:
            Fst_subtitle.subheader('Picking for {}'.format(tmp))
        if len(values_feat_choosen)>0:
            Snd_subtitle.dataframe(pd.DataFrame([(features_label[key],val) for key,val in values_feat_choosen.items()],columns=['Char.','Value']))
            show_results(values_feat_choosen)
        else:
            st.write()


#st.text('# 1) Fix values \'?\'.')
