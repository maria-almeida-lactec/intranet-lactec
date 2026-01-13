import React from 'react';
import { Container } from '@plone/components';
import type { Area } from 'volto-lactec-intranet/types/content';

interface EnderecoInfoProps {
  content: Area;
}

const EnderecoInfo: React.FC<EnderecoInfoProps> = ({ content }) => {
  const { endereco, complemento, cidade, estado, cep } = content;

  const enderecoCompleto = [
    endereco,
    complemento,
    cidade && estado ? `${cidade}/${estado}` : null,
    cep,
  ]
    .filter(Boolean)
    .join(' – ');

  return (
    <Container narrow className="endereco-info">
      <span className="label" style={{ fontWeight: 'bold' }}>
        Endereço:{' '}
      </span>
      {enderecoCompleto && <span className="endereco">{enderecoCompleto}</span>}
    </Container>
  );
};

export default EnderecoInfo;
