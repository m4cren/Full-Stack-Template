import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import Sphere from "./Sphere";

const App = () => {
    return (
        <div className="h-screen w-full">
            <Canvas>
                <directionalLight position={[0, 5, 5]} />
                <ambientLight intensity={0.3} />
                <Sphere position={[10, 4, -3]} color={"red"} radius={2} />

                <Sphere position={[5, 0, -1]} color={"blue"} radius={2} />
                <Sphere position={[5, 0, -20]} color={"yellow"} radius={2} />

                <Sphere position={[4, -2, 5]} color={"green"} radius={2} />

                <Sphere position={[0, 4, 2]} color={"pink"} radius={2} />

                <Sphere position={[-4, -2, 2]} color={"orange"} radius={2} />
                <OrbitControls />
            </Canvas>
            <div className="fixed z-1 top-[35%] left-[30%] translate-x-[-50%] translate-y=[-50%] flex flex-col gap-4">
                <div>
                    <h1 className="text-white text-8xl">My Template</h1>
                </div>

                <h2 className="text-white text-2xl">Marc Rainier Reyes</h2>
            </div>
        </div>
    );
};

export default App;
