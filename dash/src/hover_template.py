'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    return f'''
<b style="font-family:'Roboto slab';">Neighborhood: </b>%{{y}}<br>
<b style="font-family:'Roboto slab';">Year: </b>%{{x}}<br>
<b style="font-family:'Roboto slab';">Trees Planted: </b>%{{z}}
<extra></extra>
'''

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    return f'''
<b style="font-family:'Roboto slab';">Date: </b>%{{x}}<br>
<b style="font-family:'Roboto slab';">Trees: </b>%{{y}}
<extra></extra>
'''
