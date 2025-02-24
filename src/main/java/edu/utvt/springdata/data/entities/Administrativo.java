package edu.utvt.springdata.data.entities;
import edu.utvt.springdata.data.entities.UsuarioRepository;
import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@DiscriminatorValue(value ="2")
@AllArgsConstructor
@NoArgsConstructor
@Data

public class Administrativo extends UsuarioRepository {
    
    private double salario;
    
}
