filename = "CHATFILE.txt"
color  = "COLOR"

file_stripped = read_file(filename)
df = create_df(file_stripped)
emojis = emoji_count(df)
me = "Santiago Olszevicki"
other = filename[:-4].replace("_"," ")
df = add_msj_writer(df)
df = filter_messages(df)
df = df.set_index(np.array(range(len(df))))
df = split_date(df)
df = add_elapsed_days(df)
df = remove_name_from_msj(me, other, df)
word_count = count_words(df)
df.set_index(np.array(range(len(df))))
plot_daily_chat(df, color)
plt.savefig(str("daily_plot_" + other + ".jpg"),dpi=400)
plt.close()
countplotting(df, "hour", color)
plt.savefig(str("hour_count_plot_" + other + ".jpg"),dpi=400)
plt.close()
countplotting(df, "year", color)
plt.savefig(str("year_count_plot_" + other + ".jpg"),dpi=400)
plt.close()
plot_word_cloud(word_count)
plt.savefig(str("wordcloud_plot_" + other + ".jpg"),dpi=400)
plt.close()
plot_author_pie(df)
plt.savefig(str("piechart_" + other + ".jpg"),dpi=400) 
plt.close()
print(other, "done")
