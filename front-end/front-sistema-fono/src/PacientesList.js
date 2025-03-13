import React, { useState, useEffect} from 'react';
import api from './api';

const PacientesList = () => {
    const [pacientes, setPacientes] = useState([])

    useEffect(() => {
        api.get('pacientes/')
            .then(response => setPacientes(response.data))
            .catch(error => console.error('Erro ao carregar pacientes:', error));
    }, []);

    return (
        <div>
            <h1>Lista de Pacientes</h1>
            <url>
                {pacientes.map(paciente => (
                    <li key={paciente.id}>{paciente.nome}</li>
                ))}
            </url>
        </div>
    );
};

export default PacientesList;