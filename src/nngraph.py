# NeuralNetworkScene

from manim import *

class NeuralNetwork(VGroup):
    def __init__(self, layer_sizes, **kwargs):
        super().__init__(**kwargs)
        self.layers = []
        self.connections = []
        self.create_layers(layer_sizes)
        self.create_connections()

    def create_layers(self, layer_sizes):
        for i, size in enumerate(layer_sizes):
            layer = VGroup()
            for j in range(size):
                # Create a circle for each node
                circle = Circle(radius=0.3)
                layer.add(circle)
            # Arrange the nodes vertically
            layer.arrange(DOWN, buff=0.6)
            # Position the layer horizontally
            layer.move_to((i - len(layer_sizes) / 2 + 0.5) * RIGHT * 2)
            self.layers.append(layer)
            self.add(layer)

    def create_connections(self):
        for i in range(len(self.layers) - 1):
            layer1 = self.layers[i]
            layer2 = self.layers[i + 1]
            for node1 in layer1:
                for node2 in layer2:
                    # Create a line connecting two nodes
                    line = Line(
                        node1.get_center(),
                        node2.get_center(),
                        stroke_width=1,
                        color=GRAY
                    )
                    self.connections.append(line)
                    self.add(line)

class NeuralNetworkScene(Scene):
    def construct(self):
        # Get user input for layer sizes
        try:
            # input_text = input("Enter layer sizes separated by spaces (e.g., 3 4 2 1): ")
            layer_sizes = list(map(int, (3, 2, 4, 1)))# input_text.split()))
            # if len(layer_sizes) < 2:
            #     print("At least two layers are required (input and output).")
            #     return
        except ValueError:
            # print("Invalid input. Please enter integers separated by spaces.")
            pass
            # return

        # Create and display the neural network
        nn = NeuralNetwork(layer_sizes)
        self.add(nn)

        # Create input/output labels
        labels = VGroup()
        for i, size in enumerate(layer_sizes):
            label = Text(f"Layer {i+1}\n({size} nodes)")
            label.next_to(nn.layers[i], UP)
            labels.add(label)
        self.add(labels)

        # Animate the connections appearing
        self.play(*[Create(conn) for conn in nn.connections], run_time=2)
        
        # Animate the nodes appearing
        self.play(*[Create(node) for layer in nn.layers for node in layer], run_time=2)
        
        # Keep the animation running for a while
        self.wait(2)

if __name__ == "__main__":
    from manim import Scene, config
    confignewsletter.render = False
    scene = NeuralNetworkScene()
    scene.render()