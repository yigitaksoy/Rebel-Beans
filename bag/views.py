from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    grind = None
    if 'coffee_grind' in request.POST:
        grind = request.POST['coffee_grind']
    bag = request.session.get('bag', {})

    if grind:
        if item_id in list(bag.keys()):
            if grind in bag[item_id]['items_by_grind'].keys():
                bag[item_id]['items_by_grind'][grind] += quantity
            else:
                bag[item_id]['items_by_grind'][grind] = quantity
        else:
            bag[item_id] = {'items_by_grind': {grind: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
