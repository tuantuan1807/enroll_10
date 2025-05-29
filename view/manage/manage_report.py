import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from controller.student_controller import StudentController

class ReportWindow:
    def __init__(self, parent=None):
        self.report(parent)

    def report(self, parent=None):
        controller = StudentController()
        students = controller.fetch_all_students()
        total_scores = [s.math_score + s.literature_score + s.english_score for s in students]
        bins = list(range(0, 31, 2))
        labels = [f"{b}-{b+1}" for b in bins[:-1]]
        counts = [0] * (len(bins) - 1)
        for score in total_scores:
            for i in range(len(bins) - 1):
                if bins[i] <= score < bins[i + 1]:
                    counts[i] += 1
                    break
        if max(total_scores, default=0) == 30:
            counts[-1] += total_scores.count(30)

        # Vẽ biểu đồ
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(labels, counts, color='skyblue')
        ax.set_xlabel("Khoảng tổng điểm")
        ax.set_ylabel("Số lượng thí sinh")
        ax.set_title("Thống kê tổng điểm 3 môn của thí sinh")

        for bar, count in zip(bars, counts):
            ax.annotate(str(count),
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

        win = tk.Toplevel(parent)
        win.title("Biểu đồ thống kê tổng điểm")
        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)