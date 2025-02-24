package edu.utvt.springdata.data.entities.repositories;
import java.util.UUID;

import org.springframework.data.jpa.repository.JpaRepository;

import edu.utvt.springdata.data.entities.Alumno;

public interface AlumnoRepository extends JpaRepository<Alumno, UUID>{
    
}
