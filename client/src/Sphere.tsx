import { useFrame } from "@react-three/fiber";
import { useRef } from "react";
import * as THREE from "three";

interface Props {
    color: string;
    position: [number, number, number];
    radius: number;
}

const Sphere = ({ color, position, radius }: Props) => {
    const theSphereRef = useRef<THREE.Mesh>(null);

    useFrame(() => {
        if (theSphereRef.current) {
            theSphereRef.current.rotation.x += 0.005;
            theSphereRef.current.rotation.y += 0.005;
        }
    });
    return (
        <mesh ref={theSphereRef} position={position}>
            <sphereGeometry args={[radius, 30, 15]} />
            <meshStandardMaterial color={color} wireframe />
        </mesh>
    );
};

export default Sphere;
