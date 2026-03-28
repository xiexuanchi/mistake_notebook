from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QComboBox

class MistakeDialog(QDialog):
    def __init__(self, parent=None, mistake_data=None, is_view_mode=False):
        super().__init__(parent)
        self.is_view_mode = is_view_mode
        self.mistake_data = mistake_data
        
        if is_view_mode:
            self.setWindowTitle("错题详情")
        elif mistake_data:
            self.setWindowTitle("编辑错题")
        else:
            self.setWindowTitle("添加错题")
            
        self.resize(500, 400)
        
        self.subject_input = QComboBox()
        self.subject_input.addItems(["数学", "语文", "英语", "其他"])
        
        self.question_input = QTextEdit()
        self.question_input.setPlaceholderText("请输入题目详情...")
        
        self.answer_input = QTextEdit()
        self.answer_input.setPlaceholderText("请输入正确答案及解析...")
        
        if mistake_data:
            if len(mistake_data) > 4 and mistake_data[4]:
                idx = self.subject_input.findText(mistake_data[4])
                self.subject_input.setCurrentIndex(idx if idx != -1 else 0)
            self.question_input.setPlainText(mistake_data[2])
            self.answer_input.setPlainText(mistake_data[3])
            
        self.set_read_only(is_view_mode)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.addStretch()
        
        if is_view_mode:
            self.edit_btn = QPushButton("编辑")
            self.edit_btn.clicked.connect(self.enable_edit_mode)
            self.close_btn = QPushButton("关闭")
            self.close_btn.clicked.connect(self.reject)
            self.btn_layout.addWidget(self.edit_btn)
            self.btn_layout.addWidget(self.close_btn)
        else:
            self.setup_edit_buttons()
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("学科:"))
        layout.addWidget(self.subject_input)
        layout.addWidget(QLabel("题目内容:"))
        layout.addWidget(self.question_input)
        layout.addWidget(QLabel("正确答案及解析:"))
        layout.addWidget(self.answer_input)
        layout.addLayout(self.btn_layout)
        
        self.setLayout(layout)

    def set_read_only(self, read_only):
        self.subject_input.setEnabled(not read_only)
        self.question_input.setReadOnly(read_only)
        self.answer_input.setReadOnly(read_only)

    def setup_edit_buttons(self):
        # 清除现有按钮
        while self.btn_layout.count() > 1: # 留下 stretch
            item = self.btn_layout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()
                
        self.save_btn = QPushButton("保存")
        self.save_btn.clicked.connect(self.accept)
        
        self.cancel_btn = QPushButton("取消")
        self.cancel_btn.clicked.connect(self.reject)
        
        self.btn_layout.addWidget(self.save_btn)
        self.btn_layout.addWidget(self.cancel_btn)

    def enable_edit_mode(self):
        self.is_view_mode = False
        self.setWindowTitle("编辑错题")
        self.set_read_only(False)
        self.setup_edit_buttons()

    def get_data(self):
        # 由于去掉了标题输入框，这里直接用题目的前15个字符作为列表展示的标题
        question_text = self.question_input.toPlainText().strip()
        title = question_text[:15] + "..." if len(question_text) > 15 else question_text
        if not title:
            title = "未命名错题"
            
        return (
            title,
            question_text,
            self.answer_input.toPlainText().strip(),
            self.subject_input.currentText()
        )
