import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

def draw_profiling_plot(
    x_labels, y_stage_1_2, y_stage_3, y_stage_4_5, y_stage_6, y_other, filename,
    x_tick_rotation=45, mark_transpose=False, y_transpose=None):

    """
    if mark_transpose=True, mark transposeAny in distinct of stage 4_5

    Example input:


    x_labels = ['SIFT100M\nR@1=25%', 'SIFT100M\nR@10=60%', 'SIFT100M\nR@100=95%',\
        'SIFT500M\nR@1=25%', 'SIFT500M\nR@10=60%', 'SIFT500M\nR@100=95%',\
        'SIFT1000M\nR@1=25%', 'SIFT1000M\nR@10=60%', 'SIFT1000M\nR@100=95%']

    # Stage 1: OPQ
    # Stage 2: vector quantizer
    # Stage 3: select centroids
    # Stage 4: construct distance LUT
    # Stage 5: PQ code scan
    # Stage 6: collect topK results

    # input list of list, each list is [y_stage_1_2, y_stage_3, y_stage_4_5, y_stage_6, y_other] time consumption in percentage
    profile_array = [
        # 100M, 1
        [8.606278140845747, 0.11607633274229297, 3.3378707089447355, 78.57136070072978, 9.368414116737446], \
        # 100M, 10
        [32.7008185883583, 0.5164703077320218, 4.674772663594282, 33.70847203114799, 28.399466409167403]
        ]
    in this case, y_stage_1_2 = [8.606278140845747, 32.7008185883583]

    filename = generated filename
    """
    # assert input values are correct -> sum to 100
    y_all = np.array(y_stage_1_2) + np.array(y_stage_3) + \
        np.array(y_stage_4_5) + np.array(y_stage_6) + np.array(y_other)
    for y in y_all:
        assert np.isclose(y, 100)

    if mark_transpose: # 4~5 except transpose
        y_stage_4_5 = np.array(y_stage_4_5) - np.array(y_transpose)

    plt.style.use('ggplot')

    x = np.arange(len(x_labels))  # the label locations
    width = 0.4  # the width of the bars

    fig, ax = plt.subplots(1, 1, figsize=(8, 2))


    bottom_stage_1_2 = np.zeros(len(y_stage_1_2))
    bottom_stage_3 = y_stage_1_2 + bottom_stage_1_2
    if not mark_transpose:
        bottom_stage_4_5 = y_stage_3 + bottom_stage_3
    else:
        bottom_transpose =  y_stage_3 + bottom_stage_3
        bottom_stage_4_5 = y_transpose + bottom_transpose
    bottom_stage_6 = y_stage_4_5 + bottom_stage_4_5
    bottom_other = y_stage_6 + bottom_stage_6

    rects_stage_1_2 = ax.bar(x, y_stage_1_2, width, bottom=bottom_stage_1_2)
    rects_stage_3 = ax.bar(x, y_stage_3, width, bottom=bottom_stage_3)
    if mark_transpose:
        rects_transpose = ax.bar(x, y_transpose, width, bottom=bottom_transpose)
        rects_stage_4_5 = ax.bar(x, y_stage_4_5, width, bottom=bottom_stage_4_5)
    else:
        rects_stage_4_5 = ax.bar(x, y_stage_4_5, width, bottom=bottom_stage_4_5)
    rects_stage_6 = ax.bar(x, y_stage_6, width, bottom=bottom_stage_6)
    rects_other = ax.bar(x, y_other, width, bottom=bottom_other)


    label_font = 10
    tick_font = 10
    tick_label_font = 9
    legend_font = 8
    title_font = 14

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Time Consumption (%)', fontsize=label_font)
    # ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=tick_label_font)


    if mark_transpose:
        ax.legend([rects_stage_1_2, rects_stage_3, rects_stage_4_5, rects_stage_6, rects_transpose, rects_other], 
            ["Stage 1~2: OPQ + vector quantizer", "Stage 3: select centroids", \
            "Stage 4~5: construct distance LUT + scan PQ codes", "Stage 6: collect topK results", "Transpose", "Other"], loc=(0.0, 1.05), ncol=3, \
          facecolor='white', framealpha=1, frameon=False, fontsize=legend_font)
    else:
        ax.legend([rects_stage_1_2, rects_stage_3, rects_stage_4_5, rects_stage_6, rects_other], 
            ["Stage 1~2: OPQ + vector quantizer", "Stage 3: select centroids", \
            "Stage 4~5: construct distance LUT + scan PQ codes", "Stage 6: collect topK results", "Other"], loc=(0.0, 1.05), ncol=3, \
          facecolor='white', framealpha=1, frameon=False, fontsize=legend_font)


    def number_single_bar(rects, bottom, annotate_threshold=20):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for i, rect in enumerate(rects):
            height = rect.get_height()
            if height > annotate_threshold:
                ax.annotate('{:.0f}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height + bottom[i]),
                            xytext=(0, -20),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=tick_font)


    number_single_bar(rects_stage_1_2, bottom_stage_1_2, annotate_threshold=20)
    number_single_bar(rects_stage_3, bottom_stage_3, annotate_threshold=20)
    if mark_transpose:
        number_single_bar(rects_transpose, bottom_transpose, annotate_threshold=20)
    number_single_bar(rects_stage_4_5, bottom_stage_4_5, annotate_threshold=20)
    number_single_bar(rects_stage_6, bottom_stage_6, annotate_threshold=20)
    number_single_bar(rects_other, bottom_other, annotate_threshold=20)

    ax.set(ylim=[0, 100])
    plt.xticks(rotation=x_tick_rotation)
    plt.rcParams.update({'figure.autolayout': True})

    if not os.path.exists('./out_img'):
        os.mkdir('./out_img')

    plt.savefig('./out_img/{}.png'.format(filename), transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
    plt.close()