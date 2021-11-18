from tkinter import Button, Canvas, LEFT, Label, RAISED, RIGHT, Tk
from tkinter.messagebox import showerror, showinfo


class Dispenser:

  def __init__(self, window: Tk):
    self.window = window
    self.color = "black"

    self.stack = []
    self.max_size = 5
    
    
    

    # Spring
    self.spring_left = 100
    self.spring_right = 200
    self.spring_top = 100
    self.spring_bottom = 400
    self.spring_move = 50 # Distance moved by the spring
    self.spring_thickness = 2

    # New candy bar
    self.new_bar_bottom = self.spring_top + 50 
    self.new_bar_cx = (self.spring_left + self.spring_right) / 2  # Center X
    self.new_bar_cy = (self.spring_top + self.new_bar_bottom) / 2  # Center Y
    
    #spring lines
    self.a_y = self.spring_top
    self.b_y = (self.spring_top + self.spring_bottom) / 3.333333333
    self.c_y = (self.spring_top + self.spring_bottom) / 2.5
    self.d_y = (self.spring_top + self.spring_bottom) / 2
    self.e_y = (self.spring_top + self.spring_bottom) / 1.6666666667
    self.f_y = (self.spring_top + self.spring_bottom) / 1.4285714286
    self.g_y = self.spring_bottom

    self.left_panel = Canvas(self.window, width=(window_width / 2), height=window_height)
    self.left_panel.pack(side=LEFT)

    self.right_panel = Canvas(self.window, width=(window_width / 2), height=window_height)
    self.right_panel.pack(side=RIGHT)
    
    #Stack container
    self.left_panel.create_line(100,100,100,400,fill="black",width=3)
    self.left_panel.create_line(100,400,200,400,fill="black",width=3)
    self.left_panel.create_line(200,100, 200, 400, fill="black", width=3)
    
    # Draw spring
    self.a = self.left_panel.create_line(
      self.spring_left, self.a_y, self.spring_right, self.a_y, width=self.spring_thickness,
      smooth=True
    )
    self.a_b = self.left_panel.create_line(
      self.spring_left, self.b_y, self.spring_right, self.a_y, width=self.spring_thickness,
      smooth=True
    )
    self.b = self.left_panel.create_line(
      self.spring_left, self.b_y, self.spring_right, self.b_y, width=self.spring_thickness,
      smooth=True
    )
    self.b_c = self.left_panel.create_line(
      self.spring_left, self.c_y, self.spring_right, self.b_y, width=self.spring_thickness,
      smooth=True
    )
    self.c =  self.left_panel.create_line(
      self.spring_left, self.c_y, self.spring_right, self.c_y, width=self.spring_thickness,
      smooth=True
    )
    self.c_d = self.left_panel.create_line(
      self.spring_left, self.d_y, self.spring_right, self.c_y, width=self.spring_thickness,
      smooth=True
    )
    self.d = self.left_panel.create_line(
      self.spring_left, self.d_y, self.spring_right, self.d_y, width=self.spring_thickness,
      smooth=True 
    )
    self.d_e = self.left_panel.create_line(
      self.spring_left, self.e_y, self.spring_right, self.d_y, width=self.spring_thickness,
      smooth=True
    )
    self.e = self.left_panel.create_line(
      self.spring_left, self.e_y, self.spring_right, self.e_y, width=self.spring_thickness,
      smooth=True
    )
    self.e_f = self.left_panel.create_line(
      self.spring_left, self.f_y, self.spring_right, self.e_y, width=self.spring_thickness,
      smooth=True
      
    )
    self.f = self.left_panel.create_line(
      self.spring_left, self.f_y, self.spring_right, self.f_y, width=self.spring_thickness,
      smooth=True
    )
    self.f_g = self.left_panel.create_line(
      self.spring_left, self.g_y, self.spring_right, self.f_y, width=self.spring_thickness,
      smooth=True
    ) 
    self.left_panel.create_line(
      self.spring_left, self.g_y, self.spring_right, self.g_y, width=self.spring_thickness,
      smooth=True
    )

    # Buttons
    
    Button(
      self.right_panel, text="Push", fg="black", bg="green", font=("calibri", 12, "bold"),
      command=self.push
    ).place(x=52, y=155)
    Button(
      self.right_panel, text="Pop", fg="black", bg="green", font=("calibri", 12, "bold"),
      command=self.pop
    ).place(x=52, y=210)
    Button(
      self.right_panel, text="Top", fg="black", bg="green", font=("calibri", 12, "bold"),
      command=self.top
    ).place(x=52, y=266)
    Button(
      self.right_panel, text="Size", fg="black", bg="green", font=("calibri", 12, "bold"),
      command=self.report_size
    ).place(x=52, y=376)
    Button(
      self.right_panel, text="Is Empty", fg="black", bg="green",
      font=("calibri", 12, "bold"), command=self.report_empty_stat
    ).place(x=52, y=321)

  def pop(self):
    if self.size() > 0:

      candy = self.stack.pop()
      self.left_panel.delete(candy['bar'])
      self.left_panel.delete(candy['label'])

      self.update_container('pop')
    else:
      showerror(
        "Empty",
        "Stack Underflow!"
        "\n\nStack is empty"
      )

  def push(self):
    if self.size() < self.max_size:
      self.stack.append(self.make_candy())  # Add candy to stack.
      self.update_container('push')
    else:
      showerror(
        "Full",
        "Stack Overflow!"
        "\n\nStack is full"
        
        
     )  
      
      

  def make_candy(self):
    bar = self.left_panel.create_oval(
      self.spring_left, self.spring_top, self.spring_right, self.new_bar_bottom,
      fill="pink"
    )
    tag = f'Candy {self.size() + 1}'
    label = self.left_panel.create_text(
      self.new_bar_cx, self.new_bar_cy, text=tag, fill='black'
    )
    return {
      'bar': bar,
      'label': label,
      'tag': tag
    }

  def update_container(self, mode):
    # Update position of all candies excluding the topmost in the stack.
    if mode == 'push':
      for i in range(self.size()):
        self.update_candy_position(self.stack[i], (self.size() - 1) - i)

      # Update spring
      self.a_y += 50
      self.b_y +=41.7
      self.c_y +=33.3
      self.d_y += 25
      self.e_y +=16.7
      self.f_y += 8.3
      
    elif mode == 'pop':
      stack_size = self.size()
      for i in range(stack_size):
        self.update_candy_position(self.stack[i], stack_size - (i + 1))

      # Update spring.
      self.a_y -=50
      self.b_y -= 41.7
      self.c_y -= 33.3
      self.d_y -= 25
      self.e_y -=16.7
      self.f_y -= 8.3
      
    else:
      raise Exception

    # Update spring.
    self.left_panel.coords(self.a, self.spring_left, self.a_y, self.spring_right, self.a_y)
    self.left_panel.coords(self.a_b, self.spring_left, self.b_y, self.spring_right, self.a_y)
    self.left_panel.coords(self.b, self.spring_left, self.b_y, self.spring_right, self.b_y)
    self.left_panel.coords(self.b_c, self.spring_left, self.c_y, self.spring_right, self.b_y)
    self.left_panel.coords(self.c, self.spring_left, self.c_y, self.spring_right, self.c_y)
    self.left_panel.coords(self.c_d, self.spring_left, self.d_y, self.spring_right, self.c_y)
    self.left_panel.coords(self.d, self.spring_left, self.d_y, self.spring_right, self.d_y)
    self.left_panel.coords(self.d_e, self.spring_left, self.e_y, self.spring_right, self.d_y)
    self.left_panel.coords(self.e, self.spring_left, self.e_y, self.spring_right, self.e_y)
    self.left_panel.coords(self.e_f, self.spring_left, self.f_y, self.spring_right, self.e_y)
    self.left_panel.coords(self.f, self.spring_left, self.f_y, self.spring_right, self.f_y)
    self.left_panel.coords(self.f_g, self.spring_left, self.g_y, self.spring_right, self.f_y)
    
    self.left_panel.update()  # Redraw components

  def update_candy_position(self, candy, y):
    updated_bar_top = self.spring_top + (self.spring_move * y)
    updated_bar_bottom = self.new_bar_bottom + (self.spring_move * y)

    self.left_panel.coords(
      candy['bar'], self.spring_left, updated_bar_top, self.spring_right, updated_bar_bottom
    )
    self.left_panel.coords(
      candy['label'], self.new_bar_cx, (updated_bar_top + updated_bar_bottom) / 2
    )

  def size(self):
    return len(self.stack)

  def report_size(self):
    showinfo('Size', f'size of stack: {self.size()}')

  def top(self):
    if self.is_empty():
      showerror('Empty', 'The stack is empty')
    else:
      showinfo('Peek', f'Top candy is "{self.stack[-1]["tag"]}"')

  def is_empty(self):
    if self.size() == 0:
      return True
    return False

  def report_empty_stat(self):
    msg = 'False'
    if self.is_empty():
      msg = 'True'
    showinfo('Is Empty', msg)


if __name__ == '__main__':
  window_height = 600
  window_width = 700

  root = Tk()
  root.title('Candy Dispenser')
  root.maxsize(window_width, window_height)
  root.minsize(window_width, window_height)
  Dispenser(root)
  root.mainloop()
