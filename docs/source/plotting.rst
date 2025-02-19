Plotting
========

Inventory decay graphs
----------------------

The Inventory ``plot()`` method is for creating graphs of the radioactive decay
of the radionuclides in an inventory and their progeny over time. At its
simplest, specify the decay timespan to the method:

.. code-block:: python3

    >>> import radioactivedecay as rd
    >>> inv = rd.Inventory({'Rn-222': 10.0})
    >>> fig, ax = inv.plot(5, 'h')

.. image:: images/Rn-222_decay_1.png
  :width: 450

The graph shows the ingrowth of short-lived Rn-222 progeny. Use parameters such
as ``xscale``, ``yscale``, ``xmin`` and ``ymin`` to tailor the graph to your
own needs:

.. code-block:: python3

    >>> fig, ax = inv.plot(1000, 'd', xscale='log', yscale='log', xmin=1, ymin=1E-8)

.. image:: images/Rn-222_decay_2.png
  :width: 450
  
Now we can see the long-lived Pb-210 radionuclide and its progeny, which form
over a period of months. Large numbers of curves can make the graphs difficult
to read. Use the ``display`` parameter to specify only the radionuclides you
want to display. The curves follow the same order as the list you supply:

.. code-block:: python3

    >>> fig, ax = inv.plot(1000, 'd', display=['Rn-222', 'Pb-210', 'Po-210'], xscale='log', yscale='log', xmin=1, ymin=1E-8)

.. image:: images/Rn-222_decay_3.png
  :width: 450

If you wish to display all radionuclides in alphabetical order, use the
``order`` parameter:

.. code-block:: python3

    >>> fig, ax = inv.plot(5, 'h', order='alphabetical')

.. image:: images/Rn-222_decay_4.png
  :width: 450
  
The ``plot()`` method returns the Matplotlib figure and axes objects used to
create the graph. These can be used to save the figure to the file or to replot
using your own Matplotlib parameters:

.. code-block:: python3

    >>> fig.savefig('Rn-222.png', dpi=150)

For more information on handling the figure and axes objects, see the
`Matplotlib documentation <https://matplotlib.org/contents.html>`_.
