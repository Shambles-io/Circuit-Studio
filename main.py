import dearpygui.dearpygui as dpg

dpg.create_context()

## FONT ##
FONT_SCALE = 2
with dpg.font_registry():
    font_medium = dpg.add_font('assets\\Inter-Medium.ttf', 16*FONT_SCALE)
dpg.set_global_font_scale(1/FONT_SCALE)
dpg.bind_font(font_medium)


def add():
    dpg.add_input_int(parent='input_group')

def remove():
    numbers_tags = dpg.get_item_children('input_group', 1)
    if len(numbers_tags) > 1:
        dpg.delete_item(numbers_tags[-1])


def print_numbers():
    
    numbers = [dpg.get_value(tag) for tag in dpg.get_item_children('input_group', 1)]
    print(numbers)
    print(type(numbers))
    dpg.set_value('vals_list',numbers)
    dpg.show_item('vals_list')
    # dpg.add_text(f"Values: {numbers}")



with dpg.window(label="Circuit Load Calculator", tag="circuit_load_win", width=350, height=350, show=False):
    dpg.add_text("INPUT PARAMETERS")
    dpg.add_text("Power Rating of Each Device (Watts):")
    with dpg.group(tag='input_group'):
        for _ in range(4):
            dpg.add_input_int()

    with dpg.group(horizontal=True):
        dpg.add_button(label='Add Number', callback=add)
        dpg.add_button(label='Remove Last Number', callback=remove)
        dpg.add_button(label='Print Numbers', callback=print_numbers)

    dpg.add_listbox(label="Values", tag='vals_list',user_data=[2,3,4], show=False)
    






with dpg.window(label="Main Window", tag='main_win', width=450, height=450):
    dpg.add_button(label="Circuit Load Calc", tag='circuit_load_button', callback=lambda: dpg.configure_item('circuit_load_win', show=True))



    dpg.add_separator()
    dpg.add_button(label="Dev", tag="dev_btn", callback=lambda: dpg.show_debug())
    dpg.add_button(label="Demo", tag="demo", callback=lambda: dpg.show_imgui_demo())



dpg.create_viewport(title='BoilerPlate', x_pos=0, y_pos=0, width=900, height=600, clear_color=(42,113,124,255))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()