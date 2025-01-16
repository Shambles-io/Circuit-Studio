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

    if numbers:
        power_total = sum(numbers)
        circuit_voltage = dpg.get_value('circuit_voltage')
        breaker_capacity = dpg.get_value('breaker_capacity')
        # print(type(power_total))
        # print(type(dpg.get_value('circuit_voltage')))

        if circuit_voltage > 0:
            total_current = power_total / circuit_voltage
            dpg.set_value('current_total', f"Total Current: {total_current:.2f} A")

            if breaker_capacity > 0 and total_current > breaker_capacity:
                dpg.set_value('breaker_status', f"Warning: Current exceeds breaker capacity of {breaker_capacity} A!")            
            else:
                dpg.set_value('breaker_status', "Breaker Status: OK")

        else:
            dpg.set_value('current_total', "Error: Voltage must be greater than 0.")
            dpg.set_value('breaker_status', "Breaker Status: N/A")

        dpg.set_value('input_sum', f"Total Power: {power_total} W")
    else:
        dpg.set_value('input_sum', "No values entered.")
        dpg.set_value('current_total', "")
        dpg.set_value('breaker_status', "Breaker Status: N/A")




with dpg.window(label="Circuit Load Calculator", tag="circuit_load_win", width=400, height=500, show=False):
    # dpg.add_text("INPUT PARAMETERS")
    dpg.add_text("Power Rating of Each Device (Watts):")
    with dpg.group(tag='input_group'):
        for _ in range(4):
            dpg.add_input_int()

    with dpg.group(horizontal=True):
        dpg.add_button(label='Add Number', callback=add)
        dpg.add_button(label='Remove Last Number', callback=remove)
        dpg.add_button(label='Print Numbers', callback=print_numbers)

    dpg.add_separator()
    dpg.add_text("Voltage (V)")
    dpg.add_input_int(tag='circuit_voltage', default_value=120)
    
    dpg.add_separator()
    dpg.add_text("Circuit Breaker Capacity (A)")
    dpg.add_input_int(tag='breaker_capacity', default_value=20)

    dpg.add_separator()
    dpg.add_text("", tag='input_sum')
    dpg.add_text("", tag='current_total')
    dpg.add_text("", tag='breaker_status')
    


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